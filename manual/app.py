import sqlite3
from pathlib import Path

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

DATABASE = Path(__file__).parent / "guestbook.db"

def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row

    return connection

@app.route("/", methods=["GET"])
def index():

    connection = get_db_connection()

    entries = connection.execute(
        """
        SELECT id, name, message, created_at
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
        name = request.form.get("name", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not message:
            return render_template(
                "add.html",
                error="Vui lòng nhập đầy đủ tên và lời nhắn.",
                name=name,
                message=message
            )

        connection = get_db_connection()

        connection.execute(
            """
            INSERT INTO entries (name, message)
            VALUES (?, ?)
            """,
            (name, message)
        )

        connection.commit()
        connection.close()

        return redirect(url_for("index"))

    return render_template("add.html")


@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):

    connection = get_db_connection()

    connection.execute(
        """
        DELETE FROM entries
        WHERE id = ?
        """,
        (id,)
    )

    connection.commit()
    connection.close()

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)