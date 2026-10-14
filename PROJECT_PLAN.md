# Python Guestbook — Project Plan

## 1. Tổng quan dự án

**Tên dự án:** Python Guestbook  
**Tên GitHub Repository:** `python-guestbook`  
**Mô tả repo:** A Python Flask guestbook application built using Manual Coding and AI-assisted Vibe Coding.

Ứng dụng **Guestbook (Sổ lưu bút)** cho phép khách truy cập:

- Xem tất cả lời nhắn đã lưu.
- Thêm lời nhắn mới thông qua biểu mẫu.
- Xóa lời nhắn theo ID.
- Lưu trữ dữ liệu lâu dài.
- Xem thống kê số lượng lời nhắn và biểu đồ.

**Yêu cầu quan trọng:** Xây dựng **2 phiên bản độc lập**: **Manual Code** (tự viết) và **Vibe Code** (AI hỗ trợ viết code).

### Thiết lập GitHub repo

- **Repository name:** `python-guestbook`
- **Visibility:** Public (trừ khi giảng viên yêu cầu Private).
- **README:** Tạo sẵn.
- **.gitignore:** Chọn Python.
- **License:** Có thể để None.

## 2. Công nghệ sử dụng

| Thành phần | Công nghệ | Lý do |
|---|---|---|
| Backend | Python + Flask | Nhẹ, đơn giản, phù hợp bài tập |
| Frontend | HTML + CSS | Phù hợp yêu cầu HTML cơ bản |
| Template Engine | Jinja2 | Tích hợp sẵn với Flask |
| Lưu trữ ban đầu | Python List | Yêu cầu buổi 1 |
| Lưu trữ bằng file | JSON | Yêu cầu buổi 2 |
| Database | SQLite | Đáp ứng yêu cầu có DB |
| Biểu đồ | Matplotlib | Yêu cầu vẽ biểu đồ ở buổi 2 |
| Quản lý mã nguồn | Git + GitHub | Hỗ trợ làm việc nhóm |
| Vibe Code | AI Coding Assistant | Thực hiện phiên bản có AI hỗ trợ |

> **Lưu ý:** Đề bài yêu cầu sử dụng **Python List** ở buổi 1, **JSON** ở buổi 2, đồng thời có yêu cầu tổng quát là **có DB**. Vì vậy, cần hoàn thành List và JSON theo từng giai đoạn trước; sau đó bổ sung SQLite thay vì bỏ qua các giai đoạn đầu.

## 3. Kế hoạch triển khai (Roadmap)

### Phase 1 — Guestbook cơ bản (Buổi 1)

**Mục tiêu:** Xây dựng website bằng Flask và HTML cơ bản, dùng Python List toàn cục để lưu lời nhắn khi ứng dụng đang chạy.

**Chức năng:**

- `GET /`
  - Lấy toàn bộ lời nhắn từ Python List.
  - Render `index.html` với biến `entries`.
- `GET /add`
  - Hiển thị form với 2 trường `name` và `message`.
- `POST /add`
  - Kiểm tra không để trống `name` hoặc `message`.
  - Nếu hợp lệ: thêm lời nhắn và redirect về `/`.
  - Nếu không hợp lệ: hiển thị lại form kèm thông báo lỗi.
- `POST /delete/<int:id>`
  - Xóa lời nhắn có ID tương ứng.
  - Redirect về `/`.
  - *Đề bài cho phép POST hoặc GET; kế hoạch chọn POST để thao tác xóa an toàn và hợp lý hơn.*

**Kết quả cần đạt:** Website hiển thị, thêm và xóa lời nhắn được. Dữ liệu lưu trong Python List nên sẽ mất khi tắt ứng dụng ở giai đoạn này.

### Phase 2 — JSON Persistence (Buổi 2)

**Mục tiêu:** Dữ liệu không bị mất sau khi tắt hoặc khởi động lại Flask.

**Công việc:**

- Đọc dữ liệu từ `data.json` khi khởi động, nếu file tồn tại.
- Khởi tạo dữ liệu rỗng nếu chưa có file.
- Ghi lại file JSON sau mỗi lần thêm hoặc xóa lời nhắn.
- Đảm bảo mỗi lời nhắn có ID riêng để tránh xóa nhầm.

**Kết quả cần đạt:** Restart Flask vẫn giữ nguyên dữ liệu lời nhắn.

### Phase 3 — Statistics & Charts (Buổi 2)

**Mục tiêu:** Xây dựng trang thống kê kèm biểu đồ.

**Chức năng:**

- `GET /stats`: Hiển thị tổng số lời nhắn.
- Thống kê **5 người gửi nhiều lời nhắn nhất**, tính theo `name`.
- Dùng Matplotlib tạo **biểu đồ cột (bar chart)** cho số lượng lời nhắn theo người gửi.
- Xuất biểu đồ thành ảnh PNG, ví dụ `static/stats.png`.
- Nhúng ảnh biểu đồ vào `stats.html`.
- Xử lý trường hợp chưa có lời nhắn để trang thống kê không bị lỗi.

**Kết quả cần đạt:** Trang `/stats` hiển thị đúng số liệu, top 5 và biểu đồ.

### Phase 4 — SQLite Database (Hoàn thiện yêu cầu tổng quát)

**Mục tiêu:** Bổ sung Database theo yêu cầu của đề bài.

**Công việc:**

- Tạo SQLite Database.
- Tạo bảng `entries` dự kiến gồm:
  - `id`: ID lời nhắn.
  - `name`: Tên người gửi.
  - `message`: Nội dung lời nhắn.
  - `created_at`: Thời điểm tạo.
- Xử lý đọc, thêm và xóa lời nhắn qua SQLite.
- Giữ lại phần mã/dữ liệu theo giai đoạn List và JSON để chứng minh tiến trình bài tập.

**Kết quả cần đạt:** Ứng dụng có Database và các chức năng cũ vẫn hoạt động.

> SQLite là **phương án kỹ thuật đề xuất** để đáp ứng dòng yêu cầu "Có DB"; đề bài không chỉ định hệ quản trị cơ sở dữ liệu cụ thể.

### Phase 5 — Manual Code vs Vibe Code (So sánh)

**Mục tiêu:** Hoàn thiện và đối chiếu hai phiên bản có cùng yêu cầu chức năng.

**Manual Code:**

- Tự thiết kế cấu trúc và viết code.
- Hiểu rõ routes, xử lý form, Jinja2, dữ liệu và thống kê.
- Ghi lại các vấn đề và cách xử lý.

**Vibe Code:**

- Dùng AI Coding Assistant hỗ trợ sinh và chỉnh sửa code.
- Chủ động mô tả yêu cầu, chạy thử, kiểm tra và sửa lỗi.
- Ghi lại quy trình prompting và các bước đã thực hiện.

**So sánh:**

- Cấu trúc và độ dễ hiểu của mã nguồn.
- Thời gian thực hiện.
- Số lỗi phát sinh và cách sửa.
- Mức độ hoàn thành các chức năng theo đề bài.

**Kết quả cần đạt:** Hai phiên bản chạy độc lập, có tài liệu so sánh rõ ràng.

## 4. Cấu trúc thư mục đề xuất

```text
python-guestbook/
├── manual/
│   ├── app.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── add.html
│   │   └── stats.html
│   ├── static/
│   │   └── style.css
│   └── data.json
├── vibe-code/
│   ├── app.py
│   ├── templates/
│   ├── static/
│   └── data.json
├── docs/
│   ├── manual-process.md
│   ├── vibe-process.md
│   └── comparison.md
├── requirements.txt
├── .gitignore
└── README.md
```

**Giải thích:**

- `manual/`: Phiên bản tự viết code.
- `vibe-code/`: Phiên bản AI hỗ trợ phát triển.
- `docs/`: Lưu quy trình làm việc và báo cáo so sánh.
- `requirements.txt`: Các thư viện Python cần cài đặt.
- `README.md`: Giới thiệu và hướng dẫn chạy dự án.
- `.gitignore`: Loại trừ `.venv/`, cache, dữ liệu chạy thực tế và thông tin nhạy cảm nếu có.

> Cấu trúc trên là **dự kiến ban đầu**. Khi triển khai SQLite sẽ bổ sung thư mục/file tương ứng. Nếu `data.json` chỉ là dữ liệu chạy thực tế, nên đưa vào `.gitignore` và dùng một file JSON mẫu riêng để chia sẻ.

## 5. Kế hoạch kiểm thử

| Test case | Kết quả mong đợi |
|---|---|
| Truy cập `GET /` | Hiển thị danh sách lời nhắn |
| Truy cập `GET /add` | Hiển thị form thêm lời nhắn |
| Gửi lời nhắn hợp lệ | Thêm thành công, redirect về `/` |
| Để trống `name` hoặc `message` | Hiển thị thông báo lỗi |
| Xóa ID tồn tại | Xóa đúng lời nhắn |
| Xóa ID không tồn tại | Ứng dụng không bị lỗi |
| Restart Flask sau Phase 2 | Dữ liệu JSON vẫn còn |
| Truy cập `GET /stats` | Hiển thị tổng số lời nhắn và top 5 |
| Chưa có lời nhắn | Trang thống kê không bị lỗi |
| Có nhiều lời nhắn cùng `name` | Số lượng thống kê chính xác |
| Xem biểu đồ | Ảnh PNG hiển thị và phù hợp số liệu |
| Chạy hai phiên bản | Manual và Vibe Code đều hoạt động độc lập |

## 6. Thứ tự thực hiện đề xuất

1. Tạo repository `python-guestbook` trên GitHub.
2. Clone repo về máy và mở trong IDE.
3. Tạo môi trường ảo Python và cài Flask.
4. Tạo cấu trúc thư mục `manual/` và `vibe-code/`.
5. Hoàn thành **Phase 1** trong `manual/`, hiểu rõ từng route.
6. Bổ sung **Phase 2** (JSON) và **Phase 3** (thống kê, Matplotlib).
7. Bổ sung SQLite theo **Phase 4**, bảo toàn yêu cầu của những giai đoạn trước.
8. Thực hiện các chức năng tương đương trong `vibe-code/` bằng AI Assistant.
9. Kiểm thử hai phiên bản theo bảng test case.
10. Viết `README.md` và tài liệu `docs/comparison.md` để nộp hoặc trình bày.

## 7. Tiêu chí hoàn thành dự án

- [ ] Hoàn thành trang hiển thị danh sách lời nhắn.
- [ ] Hoàn thành form thêm lời nhắn có validation.
- [ ] Hoàn thành xóa lời nhắn theo ID.
- [ ] Buổi 1 có bản chạy sử dụng Python List.
- [ ] Buổi 2 có lưu và tải dữ liệu bằng JSON.
- [ ] Có trang `/stats` với tổng số lời nhắn và top 5 người gửi.
- [ ] Có biểu đồ cột được vẽ bằng Matplotlib và nhúng vào HTML.
- [ ] Có Database theo yêu cầu tổng quát.
- [ ] Có hai phiên bản **Manual** và **Vibe Code**.
- [ ] Có tài liệu hướng dẫn chạy và so sánh kết quả.

---

**Nguyên tắc triển khai:** Ưu tiên hoàn thành bản Manual trước để nắm chắc Flask, routes, templates, xử lý form và lưu trữ dữ liệu; sau đó xây dựng bản Vibe Code độc lập dựa trên cùng đặc tả chức năng để việc so sánh có ý nghĩa.
