import hashlib
from functools import lru_cache
from pathlib import Path

from django.conf import settings
from django.utils import timezone

from . import content

STATIC_DIR = Path(__file__).resolve().parent / 'static' / 'learning'


@lru_cache(maxsize=1)
def asset_version():
    """Mã phiên bản của app.css/app.js để trình duyệt tải bản mới sau mỗi lần deploy."""
    digest = hashlib.sha1()
    for name in ('css/app.css', 'js/app.js'):
        path = STATIC_DIR / name
        if path.exists():
            digest.update(path.read_bytes())
    return digest.hexdigest()[:10]


def site(request):
    today_day, today_status = content.scheduled_day(timezone.localdate())
    return {
        'SITE_NAME': settings.SITE_NAME,
        'SITE_URL': settings.SITE_URL,
        'today_day': today_day,
        'today_status': today_status,
        'ASSET_VERSION': asset_version(),
    }
