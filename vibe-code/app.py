import sqlite3

from pathlib import Path
from uuid import uuid4

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for
)

from werkzeug.utils import secure_filename


app = Flask(__name__)

BASE_DIRECTORY = Path(__file__).resolve().parent

# Đường dẫn đến database
DATABASE = BASE_DIRECTORY / "guestbook.db"

# Đường dẫn lưu ảnh người dùng tải lên
UPLOAD_FOLDER = BASE_DIRECTORY / "static" / "uploads"

# Các định dạng ảnh được chấp nhận
ALLOWED_EXTENSIONS = {
    "jpg",
    "jpeg",
    "png",
    "webp"
}

# Giới hạn toàn bộ request tối đa 5 MB
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

# Nếu thư mục uploads chưa tồn tại thì tự tạo
UPLOAD_FOLDER.mkdir(
    parents=True,
    exist_ok=True
)


def get_db_connection():

    connection = sqlite3.connect(DATABASE)

    connection.row_factory = sqlite3.Row

    return connection


def allowed_file(filename):

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in ALLOWED_EXTENSIONS
    )


@app.errorhandler(413)
def image_too_large(error):

    return render_template(
        "add.html",
        error="Ảnh quá lớn. Vui lòng chọn ảnh nhỏ hơn 5 MB.",
        name="",
        message=""
    ), 413


@app.route("/", methods=["GET"])
def index():
    connection = get_db_connection()

    entries = connection.execute(
        """
        SELECT
            id,
            name,
            message,
            created_at,
            image_filename
        FROM entries
        ORDER BY id ASC
        """
    ).fetchall()

    connection.close()

    return render_template(
        "index.html",
        entries=entries
    )


@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":
        name = request.form.get(
            "name",
            ""
        ).strip()

        message = request.form.get(
            "message",
            ""
        ).strip()

        image = request.files.get("image")

        if not name or not message:
            return render_template(
                "add.html",
                error="Vui lòng nhập đầy đủ tên và lời nhắn.",
                name=name,
                message=message
            )

        image_filename = None

        if image and image.filename:
            original_filename = secure_filename(
                image.filename
            )

            if not allowed_file(original_filename):
                return render_template(
                    "add.html",
                    error=(
                        "Ảnh không hợp lệ. "
                        "Chỉ chấp nhận JPG, JPEG, PNG hoặc WEBP."
                    ),
                    name=name,
                    message=message
                )

            # Lấy đuôi file, ví dụ: .jpg
            extension = Path(
                original_filename
            ).suffix.lower()

            # Tạo tên mới để tránh bị trùng
            image_filename = (
                f"{uuid4().hex}{extension}"
            )

            image_path = (
                UPLOAD_FOLDER / image_filename
            )

            # Lưu ảnh vào static/uploads
            image.save(image_path)

        connection = get_db_connection()

        connection.execute(
            """
            INSERT INTO entries (
                name,
                message,
                image_filename
            )
            VALUES (?, ?, ?)
            """,
            (
                name,
                message,
                image_filename
            )
        )

        connection.commit()
        connection.close()

        return redirect(
            url_for("index")
        )

    return render_template("add.html")


@app.route(
    "/delete/<int:id>",
    methods=["POST"]
)
def delete(id):
    connection = get_db_connection()

    entry = connection.execute(
        """
        SELECT image_filename
        FROM entries
        WHERE id = ?
        """,
        (id,)
    ).fetchone()

    connection.execute(
        """
        DELETE FROM entries
        WHERE id = ?
        """,
        (id,)
    )

    connection.commit()
    connection.close()

    # Nếu lưu bút có ảnh thì xóa file ảnh
    if entry and entry["image_filename"]:
        image_path = (
            UPLOAD_FOLDER
            / entry["image_filename"]
        )

        if image_path.exists():
            image_path.unlink()

    return redirect(
        url_for("index")
    )


if __name__ == "__main__":
    app.run(debug=True)