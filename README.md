# English Daily — Lộ trình tiếng Anh giao tiếp 12 tuần

Web tự học tiếng Anh giao tiếp theo lộ trình **12 tuần / 72 ngày học** (19/10/2026 → 09/01/2027), mỗi ngày 90 phút: từ nền tảng ngữ pháp, phát âm, phản xạ nói đến tiếng Anh công việc, phỏng vấn, thuyết trình và xử lý tình huống khó khi làm việc remote. Xây bằng **Django**, không cần đăng nhập, không cần database.

Website: https://english.vietdon.vn

## Mỗi ngày học có gì

| Phần | Nội dung |
|---|---|
| 🔊 Khởi động | 6 câu shadowing: máy đọc **chậm**, chừa khoảng lặng để bạn nói theo, lặp 1–5 lần; ghi âm từng câu để so sánh với giọng mẫu; chấm phát âm bằng nhận dạng giọng nói (Chrome/Edge) |
| 📗 Từ vựng | 14 từ/cụm từ riêng của ngày: IPA, nghĩa, ví dụ song ngữ, nút nghe thường và nghe chậm cho từ và câu ví dụ; nút "Nghe tất cả"; che nghĩa để tự kiểm tra |
| 💡 Kiến thức | Bài học ngắn (ngữ pháp, phát âm, mẫu câu, kỹ năng), mọi câu ví dụ đều bấm nghe được |
| 🎧 Nghe | Hội thoại/bài nói với nhiều giọng đọc khác nhau, ẩn lời khi nghe lần đầu, hiện nghĩa tiếng Việt, câu hỏi nghe hiểu, **chép chính tả** có chấm điểm, **chế độ đóng vai** (máy nói một vai, dừng chờ bạn nói vai còn lại) |
| 🎤 Nói | Câu hỏi luyện nói, **ghi âm lưu ngay trong trình duyệt**, bài nói mẫu tách câu để shadow, bảng tự chấm 4 tiêu chí ở các ngày đánh giá |
| 📖 Đọc | Bài đọc có audio, tóm tắt tiếng Việt, câu hỏi đọc hiểu |
| ✍️ Viết | Đề bài + gợi ý, ô viết tự lưu, đếm từ, **nghe máy đọc bài của chính bạn**, bài mẫu |
| ✅ Bài tập | Trắc nghiệm có giải thích ngay từng câu, lưu điểm |

Ngoài ra: **luyện thẻ từ** (5 dạng: lật thẻ, chọn nghĩa, nghe chọn từ, nghe & gõ, điền vào câu), **ôn tập ngắt quãng** kiểu Anki cho toàn bộ ~1.000 từ, trang **ôn tập Chủ nhật** cho mỗi tuần, **kho từ vựng** và **kho mẫu câu** có tìm kiếm, **thư viện bản ghi âm** (so sánh bản tuần 1 với tuần 12), tự đánh giá tuần, chuỗi ngày học, chế độ sáng/tối, sao lưu/khôi phục tiến độ.

Nội dung: 72 ngày · 1.008 từ vựng · 210 mẫu câu · 774 câu hội thoại có âm thanh · hơn 1.300 câu hỏi.

## Âm thanh

Toàn bộ âm thanh dùng giọng đọc neural của Microsoft qua thư viện [`edge-tts`](https://github.com/rany2/edge-tts) (miễn phí, nghe rất tự nhiên), có 4 tốc độ: rất chậm, chậm, bình thường, nhanh.

- File mp3 được tạo khi bấm nghe lần đầu (1–2 giây), sau đó lưu cache trên server và trình duyệt cache 1 năm.
- Trang ngày học tự tải trước âm thanh của từ vựng và câu khởi động trong nền, nên thường bấm là nghe ngay.
- Nếu server không tạo được âm thanh (mất mạng…), trang tự chuyển sang giọng đọc có sẵn của trình duyệt.
- Đổi giọng (Mỹ/Anh, nam/nữ) và tốc độ mặc định ở trang **Cài đặt**.

## Dữ liệu của bạn lưu ở đâu?

Web chỉ có một người học nên **không có tài khoản và không có database**:

- Tiến độ, điểm, bài viết, lịch ôn từ → `localStorage` của trình duyệt.
- Bản ghi âm → IndexedDB của trình duyệt (không tải lên server).
- Muốn học trên máy khác: **Cài đặt → Xuất file sao lưu**, rồi nhập vào máy kia. Bản ghi âm tải riêng ở trang Ghi âm.

## Chạy local

```powershell
python -m venv venv
venv\Scripts\pip install -r requirements.txt
$env:PYTHONUTF8 = '1'
$env:DEBUG = 'True'
venv\Scripts\python manage.py runserver   # mở http://127.0.0.1:8000
venv\Scripts\python manage.py test learning
```

Không cần `migrate` hay file `.env` (có thể tạo `.env` từ `.env.example` để ghi đè cấu hình).

## Deploy lên Render (free) với tên miền english.vietdon.vn

1. Trên Render: **New → Blueprint**, chọn repo `learn_english` (Render đọc `render.yaml`). Hoặc nếu dùng lại web service cũ: trỏ service sang repo mới, giữ **Build Command** `./build.sh` và **Start Command** `./start.sh`, rồi thêm các biến môi trường như trong `render.yaml`.
2. Trong service → **Settings → Custom Domains** → thêm `english.vietdon.vn` (Blueprint đã khai báo sẵn).
3. Ở nhà cung cấp DNS của `vietdon.vn`: tạo bản ghi **CNAME** `english` → `<tên-service>.onrender.com`. Chờ Render cấp chứng chỉ HTTPS (vài phút).
4. Có thể xóa bản ghi `vstep` cũ nếu không dùng nữa.

Lưu ý gói free: server ngủ sau 15 phút không dùng (lần mở đầu chờ ~30–60 giây) và ổ đĩa bị xóa khi khởi động lại — chỉ ảnh hưởng cache âm thanh (tự tạo lại), không ảnh hưởng tiến độ học vì tiến độ nằm trong trình duyệt.

## Cấu trúc

```
english/                 cấu hình Django (settings, urls, wsgi)
learning/
  content/week01..12.py  học liệu từng tuần (mỗi tuần 6 ngày)
  content/__init__.py    nạp, chuẩn hóa, kiểm tra học liệu; tính ngày theo lịch
  tts.py                 tạo + cache mp3 bằng edge-tts
  views.py, urls.py      các trang (function-based views)
  templates/learning/    giao diện (Bootstrap 5)
  static/learning/       css/app.css, js/app.js (phát âm thanh, ghi âm, shadowing, quiz, SRS…)
  tests.py
```

Sửa hoặc thêm nội dung: chỉnh file `learning/content/weekNN.py` (định dạng mô tả ở đầu `learning/content/__init__.py`). Lỗi định dạng (thiếu trường, đáp án ngoài lựa chọn…) sẽ báo ngay khi chạy server hoặc test.
