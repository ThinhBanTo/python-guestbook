# 🎓 Python Graduation Guestbook

Ứng dụng **Sổ lưu bút và Tường ảnh kỷ yếu tốt nghiệp**, được xây dựng bằng Python Flask.

Dự án gồm hai phiên bản:

- **Manual:** Phiên bản cơ bản, tập trung vào Flask, xử lý biểu mẫu, SQLite và giao diện bảng ghim kỷ yếu.
- **Vibe Code:** Phiên bản mở rộng có AI hỗ trợ, bổ sung upload ảnh cá nhân, xem trước ảnh và hiệu ứng nền sao băng.

**Tên repository:** `python-guestbook`

---

## 1. Ý tưởng dự án

### Chủ đề: Lưu bút ngày ra trường

Website là nơi các thành viên trong lớp lưu lại lời chúc, những câu chuyện và kỷ niệm trước ngày tốt nghiệp.

Mỗi lưu bút được trình bày dưới dạng một tấm ảnh trên bảng ghim, kèm tên người gửi. Khi bấm vào ảnh, người dùng có thể đọc toàn bộ lời nhắn trong hộp thoại chi tiết.

Giao diện sử dụng tông màu kem, nâu và màu giấy, tạo cảm giác gần gũi với một cuốn lưu bút hoặc bảng ảnh kỷ niệm.

Tiêu đề chính của website:

> **Lời tâm sự thầm kín**

### Định hướng hai phiên bản

**Manual — Bảng ghim kỷ yếu**

- Giao diện bảng ghim với ảnh minh họa và tên người gửi.
- Các chức năng cơ bản: xem, thêm và xóa lưu bút.
- Lưu dữ liệu bằng SQLite.
- Cấu trúc mã nguồn đơn giản, thuận tiện cho việc học và giải thích.

**Vibe Code — Bảng ghim tương tác**

- Giữ phong cách bảng ghim và tông màu của phiên bản Manual.
- Cho phép người dùng tải ảnh cá nhân lên.
- Xem trước ảnh và tên người gửi ngay trên trang thêm lưu bút.
- Bổ sung nền sao băng, hạt sáng và ánh sáng chuyển động.
- Có nút bật/tắt hiệu ứng nền.
- Điều chỉnh giao diện cho màn hình máy tính và điện thoại.

> Ý tưởng Vibe Code ban đầu là dây đèn treo ảnh Polaroid. Trong quá trình thực hiện, thiết kế được điều chỉnh thành bảng ghim kết hợp nền sao băng để phù hợp hơn với giao diện đã lựa chọn.

---

## 2. Trạng thái hiện tại

| Hạng mục | Trạng thái |
|---|---|
| Trang chủ hiển thị danh sách lưu bút | Đã triển khai |
| Bấm ảnh để xem chi tiết lời nhắn | Đã triển khai |
| Thêm lưu bút bằng biểu mẫu | Đã triển khai |
| Kiểm tra tên và lời nhắn không được để trống | Đã triển khai |
| Xóa lưu bút bằng phương thức POST | Đã triển khai |
| Lưu dữ liệu bằng SQLite ở cả hai phiên bản | Đã triển khai |
| Upload ảnh cá nhân trong Vibe Code | Đã triển khai |
| Xem trước ảnh và tên trong Vibe Code | Đã triển khai |
| Hiệu ứng nền sao băng trong Vibe Code | Đã triển khai |
| Nút bật/tắt hiệu ứng nền | Đã triển khai |
| Lưu và đọc dữ liệu bằng JSON | Chưa triển khai |
| Trang thống kê `/stats` | Chưa triển khai |
| Biểu đồ Top 5 bằng Matplotlib | Chưa triển khai |
| Hoàn thiện tài liệu quy trình và so sánh | Dự kiến bổ sung |

---

## 3. Công nghệ sử dụng

| Thành phần | Công nghệ | Vai trò |
|---|---|---|
| Backend | Python + Flask | Xử lý request, biểu mẫu và các route |
| Template | Jinja2 | Kết hợp dữ liệu Python với HTML |
| Frontend | HTML, CSS, Vanilla JavaScript | Xây dựng giao diện và tương tác |
| Database | SQLite | Lưu trữ lời nhắn lâu dài |
| Truy cập SQLite | Thư viện `sqlite3` | Đọc, thêm và xóa dữ liệu bằng Python |
| Lưu ảnh | Thư mục `static/uploads/` | Lưu ảnh người dùng tải lên |
| Hiệu ứng | CSS Animation | Tạo sao băng và chuyển động nền |
| Quản lý mã nguồn | Git + GitHub | Theo dõi thay đổi và làm việc nhóm |
| Chia sẻ demo | VS Code Dev Tunnels | Chia sẻ ứng dụng đang chạy trên máy local |

Các công nghệ dự kiến sử dụng tiếp:

- **JSON:** Hoàn thiện yêu cầu lưu dữ liệu bằng file ở buổi 2.
- **Matplotlib:** Vẽ biểu đồ thống kê lưu bút.

> `sqlite3` được cung cấp cùng phần lớn bản cài đặt Python thông thường. Dự án không cần cài MySQL hoặc một máy chủ SQLite riêng.

---

## 4. Chức năng của ứng dụng

### 4.1. Xem tường ảnh

Route:

```http
GET /
```

Ứng dụng đọc danh sách lưu bút từ SQLite và truyền biến `entries` sang `index.html`.

Mỗi thẻ lưu bút gồm:

- Ảnh kỷ niệm hoặc ảnh minh họa.
- Tên người gửi.
- Thao tác bấm để xem chi tiết.

### 4.2. Xem chi tiết lưu bút

Khi bấm vào một thẻ ảnh, JavaScript mở hộp thoại hiển thị:

- Ảnh của lưu bút.
- Tên người gửi.
- Toàn bộ nội dung lời nhắn.
- Nút quay lại.
- Nút xóa lưu bút.

Người dùng có thể đóng hộp thoại bằng nút đóng, nút quay lại, bấm ra ngoài hoặc nhấn `Escape`.

### 4.3. Thêm lưu bút

Các route:

```http
GET /add
POST /add
```

`GET /add` hiển thị biểu mẫu.

`POST /add` nhận dữ liệu, kiểm tra thông tin và lưu lời nhắn vào SQLite. Sau khi thêm thành công, ứng dụng chuyển về trang chủ.

Thông tin nhập:

| Trường | Ý nghĩa | Bắt buộc |
|---|---|---|
| `name` | Tên người gửi | Có |
| `message` | Nội dung lời nhắn | Có |
| `image` | Ảnh kỷ niệm, chỉ có ở Vibe Code | Không |

Biểu mẫu đặt giới hạn:

- Tên người gửi: tối đa 50 ký tự.
- Lời nhắn: tối đa 500 ký tự.

Ở Vibe Code, tên và ảnh được cập nhật ngay trong khung Polaroid xem trước.

### 4.4. Upload ảnh trong Vibe Code

Người dùng bấm vào khu vực chọn ảnh để mở cửa sổ chọn tệp trên thiết bị.

Luồng xử lý:

1. Chọn ảnh từ máy tính hoặc điện thoại.
2. JavaScript hiển thị ảnh xem trước.
3. Người dùng bấm **Đăng lưu bút**.
4. Flask nhận ảnh và lưu vào `vibe-code/static/uploads/`.
5. Database lưu tên file trong trường `image_filename`.
6. Trang chủ dùng tên file đó để hiển thị ảnh.

Định dạng hỗ trợ:

- JPG / JPEG.
- PNG.
- WEBP.

Giới hạn ảnh trên giao diện: **5 MB**. Việc kiểm tra ở backend cần được duy trì đồng bộ với giới hạn này.

> Chọn ảnh mới chỉ tạo bản xem trước. Ảnh được gửi lên server khi người dùng bấm đăng lưu bút.

Ảnh được lưu trên máy đang chạy Flask, không phải tự động lưu vào máy của người đang xem website.

### 4.5. Ảnh mặc định và ảnh dự phòng

Với lưu bút chưa có ảnh tải lên, ứng dụng sử dụng ảnh minh họa từ Picsum theo ID.

Nếu ảnh không tải được, giao diện hiển thị chữ cái đầu của tên người gửi.

Ảnh Picsum cần kết nối Internet. Ảnh đã tải lên được phục vụ từ thư mục `static/uploads/`.

### 4.6. Xóa lưu bút

Route:

```http
POST /delete/<int:id>
```

Ứng dụng xóa lưu bút theo ID rồi chuyển về trang chủ.

Trong Vibe Code, phần xử lý xóa còn dọn file ảnh upload gắn với lưu bút theo logic đã triển khai trong backend.

### 4.7. Hiệu ứng nền trong Vibe Code

Trang chủ và trang thêm lưu bút có:

- Sao băng màu đồng chuyển động liên tục.
- Hạt sáng trang trí.
- Các vùng ánh sáng nền chuyển động chậm.
- Nút bật/tắt hiệu ứng.

Hiệu ứng được xây dựng bằng CSS Animation. JavaScript điều khiển trạng thái bật/tắt và tạm dừng khi tab không hiển thị.

Giao diện tôn trọng cài đặt giảm chuyển động của thiết bị thông qua:

```css
prefers-reduced-motion: reduce
```

---

## 5. Lưu trữ dữ liệu

### 5.1. Giai đoạn Python List

Ở giai đoạn đầu, lời nhắn được lưu trong một Python List toàn cục:

```python
entries = [
    {
        "id": 1,
        "name": "Minh Đức",
        "message": "Chúc mọi người có một ngày tốt nghiệp đáng nhớ!"
    }
]
```

Dữ liệu trong List chỉ tồn tại trong bộ nhớ của tiến trình đang chạy. Các thay đổi sẽ mất khi ứng dụng khởi động lại.

### 5.2. Phiên bản hiện tại: SQLite

Cả Manual và Vibe Code hiện sử dụng SQLite để lưu dữ liệu lâu dài.

Hai phiên bản có hai database riêng:

```text
manual/guestbook.db
vibe-code/guestbook.db
```

Điều này có nghĩa:

- Thêm hoặc xóa lưu bút ở Manual không tự thay đổi dữ liệu của Vibe Code.
- Sao chép database chỉ tạo một bản sao tại thời điểm sao chép.
- Tắt server không làm mất dữ liệu đã ghi thành công vào database.

### 5.3. Bảng dữ liệu

Các trường cơ bản của bảng `entries`:

| Trường | Ý nghĩa |
|---|---|
| `id` | Khóa chính của lưu bút |
| `name` | Tên người gửi |
| `message` | Nội dung lời nhắn |
| `created_at` | Thời điểm tạo |

Vibe Code bổ sung:

| Trường | Ý nghĩa |
|---|---|
| `image_filename` | Tên file ảnh đã tải lên, có thể để trống |

Database lưu **tên file ảnh**; nội dung ảnh nằm trong thư mục `static/uploads/`.

> Sao lưu Vibe Code cần sao lưu cả `guestbook.db` và thư mục `static/uploads/`.

### 5.4. Phần JSON chưa hoàn thành

Theo kế hoạch bài tập ban đầu, JSON là yêu cầu của buổi 2.

Hiện tại, ứng dụng đã chuyển sang SQLite nhưng chưa triển khai đọc/ghi `data.json`.

Việc có SQLite không đồng nghĩa với việc đã hoàn thành yêu cầu JSON. Phần này sẽ được bổ sung riêng trong giai đoạn tiếp theo.

Khi triển khai, cần xác định rõ vai trò của JSON, chẳng hạn:

- Phiên bản lưu trữ của giai đoạn buổi 2.
- Chức năng xuất/nhập hoặc sao lưu dữ liệu.

Chưa có cơ chế đồng bộ tự động giữa List, JSON và SQLite trong phiên bản hiện tại.

---

## 6. Cấu trúc thư mục hiện tại

```text
python-guestbook/
├── docs/
│   ├── .gitignore
│   ├── README.md
│   └── requirements.txt
│
├── manual/
│   ├── app.py
│   ├── init_db.py
│   ├── guestbook.db
│   ├── templates/
│   │   ├── index.html
│   │   └── add.html
│   └── static/
│       └── style.css
│
└── vibe-code/
    ├── app.py
    ├── init_db.py
    ├── guestbook.db
    ├── templates/
    │   ├── index.html
    │   └── add.html
    └── static/
        ├── style.css
        ├── add.css
        └── uploads/
```

### Vai trò các file

| File hoặc thư mục | Vai trò |
|---|---|
| `app.py` | Khởi tạo Flask và xử lý các route |
| `init_db.py` | Script khởi tạo database |
| `guestbook.db` | Database SQLite của từng phiên bản |
| `templates/index.html` | Hiển thị tường ảnh và hộp thoại lời nhắn |
| `templates/add.html` | Biểu mẫu thêm lưu bút |
| `static/style.css` | CSS giao diện và hiệu ứng dùng chung |
| `vibe-code/static/add.css` | Điều chỉnh riêng cho trang thêm lưu bút |
| `static/uploads/` | Chứa ảnh người dùng tải lên |
| `requirements.txt` | Danh sách thư viện cần cài đặt |

**Đề xuất sắp xếp repository:** chuyển `README.md`, `requirements.txt` và `.gitignore` từ `docs/` ra thư mục gốc.

README ở thư mục gốc thuận tiện cho việc giới thiệu repository trên GitHub. `.gitignore` ở thư mục gốc có thể áp dụng cho cả `manual/`, `vibe-code/` và môi trường ảo.

> Nếu `.gitignore` chỉ nằm trong `docs/`, các quy tắc trong đó không áp dụng cho hai thư mục ứng dụng nằm bên ngoài `docs/`.

---

## 7. Cài đặt và chạy ứng dụng

Các lệnh dưới đây sử dụng PowerShell, bắt đầu từ thư mục gốc `python-guestbook`.

### 7.1. Tạo môi trường ảo

```powershell
python -m venv .venv
```

Kích hoạt môi trường:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 7.2. Cài thư viện

Theo cấu trúc hiện tại:

```powershell
python -m pip install -r docs/requirements.txt
```

Nếu đã chuyển `requirements.txt` ra thư mục gốc:

```powershell
python -m pip install -r requirements.txt
```

Ứng dụng hiện tại cần Flask. `sqlite3` và `pathlib` thuộc thư viện chuẩn của Python, không cần khai báo như các gói pip riêng.

### 7.3. Chạy Manual

```powershell
cd manual
python app.py
```

Mở trình duyệt:

```text
http://127.0.0.1:5000
```

### 7.4. Chạy Vibe Code

Dừng server đang chạy bằng `Ctrl + C`.

Từ thư mục gốc:

```powershell
cd vibe-code
python app.py
```

Mở trình duyệt:

```text
http://127.0.0.1:5000
```

Hai phiên bản mặc định cùng dùng cổng `5000`, nên chạy lần lượt hoặc cấu hình hai cổng khác nhau nếu muốn mở đồng thời.

### 7.5. Khởi tạo database khi chưa có

Trong thư mục của phiên bản tương ứng:

```powershell
python init_db.py
```

Sau đó chạy ứng dụng:

```powershell
python app.py
```

Nếu đã có dữ liệu, cần kiểm tra nội dung script trước khi chạy lại để tránh ghi đè hoặc tạo lại dữ liệu ngoài ý muốn.

---

## 8. Chia sẻ demo bằng VS Code Dev Tunnels

Link demo đã sử dụng trong quá trình phát triển:

[https://fjsllsl5-5000.asse.devtunnels.ms/](https://fjsllsl5-5000.asse.devtunnels.ms/)

Link phụ thuộc vào:

- Máy chạy ứng dụng vẫn đang bật.
- Flask đang chạy.
- Cổng tương ứng được chia sẻ qua Dev Tunnels.
- Quyền truy cập tunnel được cấu hình phù hợp.

Đây là đường dẫn chia sẻ server phát triển local, không phải một website đã triển khai hoạt động liên tục.

Phiên bản được hiển thị qua tunnel là ứng dụng đang chạy trên cổng được chia sẻ tại thời điểm đó.

---

## 9. Những vấn đề đã xử lý trong quá trình phát triển

### Chuyển từ List sang SQLite

Ban đầu, dữ liệu thêm mới mất khi ứng dụng khởi động lại.

Ứng dụng được chuyển sang SQLite để lưu dữ liệu lâu dài.

### Hai phiên bản sử dụng hai database riêng

Sau khi sao chép database từ Manual sang Vibe Code, hai file hoạt động độc lập.

Các thay đổi tiếp theo không tự đồng bộ giữa hai phiên bản.

### Bổ sung trường ảnh vào database

Khi backend bắt đầu truy vấn `image_filename` nhưng database cũ chưa có trường này, SQLite báo:

```text
sqlite3.OperationalError: no such column: image_filename
```

Cách xử lý là cập nhật cấu trúc bảng của đúng database Vibe Code.

`CREATE TABLE IF NOT EXISTS` không tự bổ sung cột mới vào một bảng đã tồn tại.

### Điều chỉnh giao diện và font chữ

Giao diện được sửa nhiều lần để:

- Cân đối cỡ chữ và khoảng cách.
- Hiển thị tên tiếng Việt rõ ràng.
- Giảm bo góc và các chi tiết trang trí không phù hợp.
- Giữ phong cách giấy, bảng ghim và ảnh kỷ niệm.
- Tăng độ rõ của hiệu ứng sao băng trên nền sáng.

### Thiết kế lại trang thêm lưu bút

Trang thêm lưu bút của Vibe Code được bổ sung:

- Khung ảnh Polaroid xem trước.
- Tên người gửi cập nhật theo nội dung đang nhập.
- Bộ đếm ký tự lời nhắn.
- Khu vực chọn ảnh có thiết kế riêng.
- Nút bỏ ảnh đã chọn.
- Nhãn và tiêu đề được điều chỉnh để dễ đọc hơn.

---

## 10. So sánh Manual và Vibe Code

| Tiêu chí | Manual | Vibe Code |
|---|---|---|
| Backend | Flask | Flask |
| Database | SQLite riêng | SQLite riêng |
| Xem, thêm, xóa lưu bút | Có | Có |
| Hộp thoại xem chi tiết | Có | Có |
| Giao diện bảng ghim | Có | Có |
| Ảnh minh họa theo ID | Có | Có khi chưa upload ảnh |
| Upload ảnh cá nhân | Không | Có |
| Xem trước ảnh trong form | Không | Có |
| Xem trước tên người gửi | Không | Có |
| Nền sao băng | Không | Có |
| Bật/tắt hiệu ứng nền | Không | Có |
| Vai trò | Phiên bản cơ bản | Phiên bản mở rộng có AI hỗ trợ |

Phần đánh giá thời gian thực hiện, lỗi phát sinh và quy trình prompting sẽ được ghi lại trong tài liệu riêng.

---

## 11. Kế hoạch tiếp theo

- [ ] Hoàn thành yêu cầu lưu dữ liệu bằng JSON của buổi 2.
- [ ] Xây dựng route `/stats`.
- [ ] Hiển thị tổng số lưu bút.
- [ ] Thống kê Top 5 người gửi nhiều lời nhắn nhất.
- [ ] Vẽ biểu đồ cột bằng Matplotlib.
- [ ] Xử lý trang thống kê khi chưa có dữ liệu.
- [ ] Bổ sung `stats.html`.
- [ ] Hoàn thiện tài liệu quá trình thực hiện Manual.
- [ ] Ghi lại quy trình sử dụng AI trong Vibe Code.
- [ ] Viết tài liệu so sánh hai phiên bản.
- [ ] Kiểm tra lại chức năng và giao diện trước khi nộp bài.

---

## 12. Phạm vi sử dụng hiện tại

Dự án phục vụ học tập và chia sẻ demo trong nhóm/lớp.

Phiên bản hiện tại chưa có hệ thống tài khoản hoặc phân quyền quản trị. Chức năng xóa cần được bổ sung kiểm soát quyền nếu mở ứng dụng cho nhiều người sử dụng công khai.