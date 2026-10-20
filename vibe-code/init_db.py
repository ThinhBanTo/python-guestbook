import sqlite3
from pathlib import Path


database_path = Path(__file__).parent / "guestbook.db"

connection = sqlite3.connect(database_path)


# Tạo bảng nếu bảng chưa tồn tại
connection.execute(
    """
    CREATE TABLE IF NOT EXISTS entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        message TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
)


# Kiểm tra bảng đang có bao nhiêu lời nhắn
total_entries = connection.execute(
    "SELECT COUNT(*) FROM entries"
).fetchone()[0]


# Chỉ thêm dữ liệu mẫu nếu bảng đang trống
if total_entries == 0:
    sample_entries = [
        (
            "Minh Đức",
            "Chúc cả lớp ra trường đều làm đúng đam mê, lương nghìn đô nhé!"
        ),
        (
            "Hoàng Nam",
            "Cảm ơn anh em đã gánh team qua những đêm chạy deadline môn Lập trình Web Python!"
        ),
        (
            "Thu Hà",
            "Sẽ nhớ mãi những buổi trà đá cổng trường sau giờ học. Hẹn gặp lại!"
        ),
        (
            "Tuấn Anh",
            "Tạm biệt giảng đường! Chúc mọi người chân cứng đá mềm trên chặng đường sắp tới."
        ),
        (
            "Khánh Linh",
            "Xin lỗi đứa ngồi cạnh vì 4 năm qua toàn mượn bút không trả nhé haha."
        ),
        (
            "Quốc Bảo",
            "Hẹn 5 năm nữa họp lớp đầy đủ không thiếu một ai!"
        )
    ]

    connection.executemany(
        """
        INSERT INTO entries (name, message)
        VALUES (?, ?)
        """,
        sample_entries
    )

    print("Đã thêm 6 lời nhắn mẫu vào database!")
else:
    print("Database đã có dữ liệu, không thêm lại dữ liệu mẫu.")


connection.commit()
connection.close()

print("Khởi tạo database thành công!")