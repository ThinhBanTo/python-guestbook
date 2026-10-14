# 🎓 Python Graduation Guestbook — Project Plan & Documentation

## 1. Tổng quan dự án

**Tên dự án:** Python Graduation Guestbook (Sổ Lưu Bút & Tường Ảnh Kỷ Yếu Tốt Nghiệp)  
**Tên GitHub Repository:** `python-guestbook`  
**Mô tả repo:** A Python Flask graduation memory wall & guestbook application built using Manual Coding and AI-assisted Vibe Coding.

### 🌐 Link Demo Trực Tiếp (Live Local Tunnel)
Khi máy chủ local đang chạy và bật cổng chia sẻ (Port Forwarding qua VS Code Dev Tunnels), các thành viên trong nhóm có thể truy cập trực tiếp giao diện mẫu tại đây để tham khảo:
👉 **Link xem Demo:** [https://fjsllsl5-5000.asse.devtunnels.ms/](https://fjsllsl5-5000.asse.devtunnels.ms/)  
*(Lưu ý: Link hoạt động khi máy chủ phát triển đang mở ứng dụng Flask ở cổng `5000`).*

---

### 💡 Ý tưởng chủ đề (Concept): "Lưu Bút Ngày Ra Trường"
Thay vì làm một trang Guestbook dạng danh sách văn bản đơn thuần, dự án được thiết kế theo chủ đề **Kỷ yếu & Lễ tốt nghiệp**, nơi mỗi lời nhắn (`entries`) được thể hiện như một **bức ảnh kỷ niệm kèm lời nhắn nhủ trước khi ra trường**:
- **Trải nghiệm tương tác:** Trên trang chủ (`/`), các lời nhắn được hiển thị dưới dạng các tấm thẻ ảnh gắn kèm tên người gửi (`name`). Khi người dùng **bấm (click) vào từng tấm ảnh**, một hộp thoại chi tiết (Modal) sẽ hiện ra giữa màn hình hiển thị bức ảnh phóng to, toàn bộ tâm thư/lời chúc (`message`) và nút xóa lời nhắn theo `ID`.
- **Thực hiện qua 2 phiên bản độc lập** (giữ nguyên 100% cấu trúc dữ liệu `id`, `name`, `message` của đề bài):
  1. **Manual Code (`manual/` — Bảng Ghim Kỷ Yếu):** Giao diện tự code tay theo phong cách **Bảng gỗ bần (Corkboard)** với các tấm ảnh vuông vức gắn đinh ghim, dùng HTML/CSS/JS thuần cơ bản, tối giản và dễ giải thích từng dòng lệnh.
  2. **Vibe Code (`vibe-code/` — Dây Đèn Treo Ảnh Polaroid):** Giao diện có AI hỗ trợ tạo hiệu ứng **Dây treo ảnh Polaroid đung đưa** (`CSS Keyframes Animation`) và hiệu ứng thẻ trượt mượt mà khi mở xem lời nhắn.

Ứng dụng cho phép khách truy cập:
- Xem tất cả thẻ ảnh lưu bút đã lưu trên bảng/dây treo.
- Click vào từng bức ảnh để đọc chi tiết lời nhắn trong lễ tốt nghiệp.
- Thêm lưu bút mới thông qua biểu mẫu (`name`, `message`).
- Xóa lưu bút theo `ID` ngay trong khung xem chi tiết.
- Lưu trữ dữ liệu lâu dài (JSON & SQLite).
- Xem thống kê tổng số lời chúc và biểu đồ Top 5 người tích cực viết lưu bút nhất.

### Thiết lập GitHub repo
- **Repository name:** `python-guestbook`
- **Visibility:** Public (trừ khi giảng viên yêu cầu Private).
- **README:** Tạo sẵn.
- **.gitignore:** Chọn Python.
- **License:** Có thể để None.

---

## 2. Công nghệ sử dụng

| Thành phần | Công nghệ | Lý do |
|---|---|---|
| Backend | Python + Flask | Nhẹ, đơn giản, phù hợp bài tập |
| Frontend | HTML + CSS + Vanilla JS | Phù hợp yêu cầu HTML cơ bản & xử lý click mở thẻ ảnh |
| Template Engine | Jinja2 | Tích hợp sẵn với Flask |
| Lưu trữ ban đầu | Python List | Yêu cầu buổi 1 |
| Lưu trữ bằng file | JSON (`data.json`) | Yêu cầu buổi 2 |
| Database | SQLite (`guestbook.db`) | Đáp ứng yêu cầu có DB |
| Biểu đồ | Matplotlib | Yêu cầu vẽ biểu đồ cột ở buổi 2 |
| Chia sẻ Demo | VS Code Dev Tunnels | Chia sẻ localhost (`:5000`) cho cả nhóm xem trực tiếp |
| Quản lý mã nguồn | Git + GitHub | Hỗ trợ làm việc nhóm |
| Vibe Code | AI Coding Assistant | Thực hiện phiên bản có AI hỗ trợ |

> **Lưu ý:** Đề bài yêu cầu sử dụng **Python List** ở buổi 1, **JSON** ở buổi 2, đồng thời có yêu cầu tổng quát là **có DB**. Vì vậy, cần hoàn thành List và JSON theo từng giai đoạn trước; sau đó bổ sung SQLite thay vì bỏ qua các giai đoạn đầu.

---

## 3. Kế hoạch triển khai (Roadmap)

### Phase 1 — Guestbook cơ bản (Buổi 1)

**Mục tiêu:** Xây dựng website Lưu bút tốt nghiệp bằng Flask và HTML cơ bản, dùng Python List toàn cục để lưu lời nhắn khi ứng dụng đang chạy.

**Chức năng:**
- `GET /`
  - Lấy toàn bộ lời nhắn từ Python List.
  - Render `index.html` với biến `entries` dưới dạng các tấm ảnh ghim trên bảng/dây.
  - Bấm vào từng ảnh để xem chi tiết `name`, `message` và nút xóa.
- `GET /add`
  - Hiển thị form viết lưu bút mới với 2 trường `name` (Tên tân cử nhân) và `message` (Điều muốn nói trong lễ tốt nghiệp).
- `POST /add`
  - Kiểm tra không để trống `name` hoặc `message`.
  - Nếu hợp lệ: thêm lời nhắn và redirect về `/`.
  - Nếu không hợp lệ: hiển thị lại form kèm thông báo lỗi.
- `POST /delete/<int:id>`
  - Xóa thẻ lưu bút có ID tương ứng.
  - Redirect về `/`.
  - *Đề bài cho phép POST hoặc GET; kế hoạch chọn POST để thao tác xóa an toàn và hợp lý hơn.*

**Kết quả cần đạt:** Website hiển thị bảng/dây ảnh lưu bút, bấm vào xem chi tiết, thêm và xóa lời nhắn được. Dữ liệu lưu trong Python List nên sẽ mất khi tắt ứng dụng ở giai đoạn này.

### Phase 2 — JSON Persistence (Buổi 2)

**Mục tiêu:** Dữ liệu lưu bút không bị mất sau khi tắt hoặc khởi động lại Flask.

**Công việc:**
- Đọc dữ liệu từ `data.json` khi khởi động, nếu file tồn tại.
- Khởi tạo dữ liệu mẫu/rỗng nếu chưa có file.
- Ghi lại file JSON sau mỗi lần thêm hoặc xóa lời nhắn.
- Đảm bảo mỗi lời nhắn có ID riêng để tránh xóa nhầm và tự động gắn ảnh kỷ niệm tương ứng theo ID.

**Kết quả cần đạt:** Restart Flask vẫn giữ nguyên các bức ảnh và lời nhắn lưu bút.

### Phase 3 — Statistics & Charts (Buổi 2)

**Mục tiêu:** Xây dựng trang thống kê độ sôi nổi của bảng lưu bút kèm biểu đồ.

**Chức năng:**
- `GET /stats`: Hiển thị tổng số lời nhắn lưu bút đã ghi.
- Thống kê **Top 5 người gửi nhiều lời nhắn nhất**, tính theo `name`.
- Dùng Matplotlib tạo **biểu đồ cột (bar chart)** minh họa số lượng lời nhắn theo người gửi.
- Xuất biểu đồ thành ảnh PNG tại `static/stats.png`.
- Nhúng ảnh biểu đồ vào `stats.html`.
- Xử lý trường hợp chưa có lời nhắn để trang thống kê không bị lỗi.

**Kết quả cần đạt:** Trang `/stats` hiển thị đúng số liệu, danh sách Top 5 và biểu đồ cột.

### Phase 4 — SQLite Database (Hoàn thiện yêu cầu tổng quát)

**Mục tiêu:** Bổ sung Database theo yêu cầu của đề bài.

**Công việc:**
- Tạo SQLite Database (`guestbook.db`).
- Tạo bảng `entries` gồm:
  - `id`: ID lời nhắn (Khóa chính tự tăng).
  - `name`: Tên người gửi.
  - `message`: Nội dung lời nhắn tốt nghiệp.
  - `created_at`: Thời điểm tạo.
- Xử lý đọc, thêm và xóa lời nhắn qua SQLite, đồng thời đồng bộ với Python List và `data.json` để bảo toàn yêu cầu của các giai đoạn trước.

**Kết quả cần đạt:** Ứng dụng có Database hoạt động ổn định cùng toàn bộ chức năng cũ.

> SQLite là **phương án kỹ thuật đề xuất** để đáp ứng dòng yêu cầu "Có DB"; đề bài không chỉ định hệ quản trị cơ sở dữ liệu cụ thể.

### Phase 5 — Manual Code vs Vibe Code (So sánh)

**Mục tiêu:** Hoàn thiện và đối chiếu hai phiên bản có cùng yêu cầu chức năng và cùng chủ đề Lưu bút tốt nghiệp.

**Manual Code (`manual/`):**
- Tự thiết kế cấu trúc và viết code giao diện **Bảng ghim kỷ yếu (Corkboard)** vuông vức, mộc mạc.
- Hiểu rõ routes, xử lý form, Jinja2, sự kiện click mở hộp thoại cơ bản, lưu trữ dữ liệu và thống kê.
- Ghi lại các vấn đề và cách xử lý.

**Vibe Code (`vibe-code/`):**
- Dùng AI Coding Assistant hỗ trợ sinh và chỉnh sửa code giao diện **Dây đèn treo ảnh Polaroid** với hiệu ứng đung đưa và thẻ trượt hiện đại.
- Chủ động mô tả yêu cầu, chạy thử, kiểm tra và sửa lỗi.
- Ghi lại quy trình prompting và các bước đã thực hiện.

**So sánh:**
- Cấu trúc và độ dễ hiểu của mã nguồn (HTML/CSS thuần tự viết vs CSS Animation do AI sinh).
- Thời gian thực hiện.
- Số lỗi phát sinh và cách sửa.
- Mức độ hoàn thành các chức năng theo đề bài.

**Kết quả cần đạt:** Hai phiên bản chạy độc lập, có tài liệu so sánh rõ ràng.

---

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
│   │   ├── index.html
│   │   ├── add.html
│   │   └── stats.html
│   ├── static/
│   └── data.json
├── docs/
│   ├── manual-process.md
│   ├── vibe-process.md
│   └── comparison.md
├── requirements.txt
├── .gitignore
└── README.md
