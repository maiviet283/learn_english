"""
Django settings cho English Daily — web tự học tiếng Anh giao tiếp theo lộ trình từng ngày.

Web chỉ có một người học nên không có đăng nhập, không có database:
- Nội dung học nằm trong code Python (learning/content/).
- Tiến độ, điểm, bài viết lưu trong trình duyệt (localStorage), bản ghi âm lưu trong IndexedDB.
- Âm thanh tạo bằng giọng đọc neural (edge-tts) và cache ra đĩa (learning/tts.py).
"""

import os
from datetime import date
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')


def env_list(name, default):
    return [x.strip() for x in os.environ.get(name, default).split(',') if x.strip()]


SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-only-key-english-daily-not-for-secrets')

DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Các host luôn được phép (kể cả khi biến môi trường ALLOWED_HOSTS điền thiếu), cộng thêm host trong
# ALLOWED_HOSTS và tên miền Render tự cấp qua RENDER_EXTERNAL_HOSTNAME.
_BASE_HOSTS = ['localhost', '127.0.0.1', '.onrender.com', 'english.vietdon.vn']
ALLOWED_HOSTS = list(dict.fromkeys(
    _BASE_HOSTS + env_list('ALLOWED_HOSTS', '') + env_list('RENDER_EXTERNAL_HOSTNAME', '')
))

CSRF_TRUSTED_ORIGINS = list(dict.fromkeys(
    ['https://english.vietdon.vn', 'https://*.onrender.com'] + env_list('CSRF_TRUSTED_ORIGINS', '')
))


INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'learning',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'english.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'learning.context_processors.site',
            ],
        },
    },
]

WSGI_APPLICATION = 'english.wsgi.application'

# Không dùng database: nội dung nằm trong code, tiến độ nằm trong trình duyệt.
DATABASES = {}

LANGUAGE_CODE = 'vi'
TIME_ZONE = 'Asia/Ho_Chi_Minh'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STORAGES = {
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedStaticFilesStorage',
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --- Cấu hình riêng của English Daily ---

SITE_NAME = 'English Daily'
SITE_URL = os.environ.get('SITE_URL', 'https://english.vietdon.vn').rstrip('/')

# Ngày bắt đầu lộ trình (thứ Hai của tuần 1). Đổi qua biến môi trường COURSE_START_DATE=YYYY-MM-DD.
COURSE_START_DATE = date.fromisoformat(os.environ.get('COURSE_START_DATE', '2026-10-19'))

# Thư mục cache file mp3 của giọng đọc. Trên Render free ổ đĩa bị xóa khi khởi động lại — không sao,
# file sẽ được tạo lại khi cần, và trình duyệt cũng tự cache.
TTS_CACHE_DIR = Path(os.environ.get('TTS_CACHE_DIR', BASE_DIR / '.tts_cache'))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {'console': {'class': 'logging.StreamHandler'}},
    'root': {'handlers': ['console'], 'level': 'WARNING'},
}
