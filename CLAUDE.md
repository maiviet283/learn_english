# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**English Daily** — web tự học tiếng Anh giao tiếp theo lộ trình 12 tuần (72 ngày học, 19/10/2026 → 09/01/2027), dựa trên file PDF "Lộ trình tiếng Anh 3 tháng" của người dùng. Django 6, một app duy nhất `learning`. UI tiếng Việt (`LANGUAGE_CODE = 'vi'`, timezone `Asia/Ho_Chi_Minh`). Chỉ một người học: **không đăng nhập, không database**. Deploy Render free, domain `english.vietdon.vn`.

## Commands

Windows, venv trong repo. **Luôn đặt `PYTHONUTF8=1`** (nội dung tiếng Việt):

```powershell
$env:PYTHONUTF8 = '1'
venv\Scripts\python manage.py runserver      # dev server (cổng 8000); preview_start tên "english"
venv\Scripts\python manage.py test learning  # test (SimpleTestCase, không cần DB)
venv\Scripts\pip install <package>
```

Không có migrate/makemigrations — `DATABASES = {}`.

## Architecture

- `english/` — project config. `settings.py` đọc `.env` (tùy chọn) qua python-dotenv; mọi biến đều có mặc định: `SECRET_KEY`, `DEBUG` (mặc định False), `ALLOWED_HOSTS`, `SITE_URL`, `COURSE_START_DATE` (thứ Hai tuần 1), `TTS_CACHE_DIR`.
- `learning/content/` — **toàn bộ học liệu là code Python**: `week01.py`…`week12.py`, mỗi file một dict `WEEK` có đúng 6 ngày. Dữ liệu viết dạng tuple cho gọn; `content/__init__.py` chuẩn hóa thành dict, đánh số ngày, tính ngày tháng, tự chọn câu chép chính tả, và **raise `ContentError` khi import nếu sai định dạng** (định dạng một ngày mô tả trong docstring đầu file). Từ vựng phải duy nhất toàn lộ trình (khóa SRS = từ viết thường; có test kiểm tra).
- `learning/tts.py` + view `/tts/?t=&v=&s=` — tạo mp3 bằng `edge-tts` (giọng Microsoft neural), cache theo sha1 ra đĩa, trả `Cache-Control: immutable`. Giọng/tốc độ chỉ cho phép trong `VOICES`/`SPEEDS`. Lỗi → 503, JS tự fallback sang Web Speech API.
- `learning/views.py` — function-based views, render template server-side; dữ liệu cho JS truyền qua `json_script`.
- `learning/static/learning/js/app.js` — toàn bộ tương tác phía client: `Store` (tiến độ trong localStorage, key `englishDaily:v1`), `Speech` (phát/huỷ âm thanh, fallback), `Seq` (chuỗi phát dừng được), shadowing player, dialogue player (đóng vai), quiz, dictation, writing autosave, recorder (IndexedDB `englishDaily`), SRS kiểu Leitner, practice modes, trang settings (xuất/nhập sao lưu).
- Templates trong `learning/templates/learning/` kế thừa `base.html`; partials ở `partials/` (`_quiz`, `_shadow`, `_vocab_cards`, `_practice`). Thẻ `{% say text 'slow' %}` (templatetags/learning_tags.py) tạo nút phát âm. Trong HTML bài học: `.say` = chữ bấm nghe được, `.ex/.fix` có `.en` sẽ được JS gắn nút loa.
- Trang: `/` · `/hom-nay/` · `/lo-trinh/` · `/tuan/<n>/` · `/tuan/<n>/on-tap/` (Chủ nhật) · `/ngay/<n>/` · `/ngay/<n>/luyen-tu/` · `/on-tap/` (SRS) · `/tu-vung/` · `/mau-cau/` · `/ghi-am/` · `/cai-dat/`.

## Deploy

`build.sh` (pip install + collectstatic + check) và `start.sh` (gunicorn gthread 2×8). `render.yaml` là Blueprint (có `domains: english.vietdon.vn`). Ổ đĩa Render free không bền — chỉ chứa cache âm thanh, không có dữ liệu người dùng.
