"""
Giọng đọc neural cho toàn site.

Dùng edge-tts (giọng Microsoft Neural — rất tự nhiên, miễn phí) để tạo file mp3 khi có người bấm
nghe lần đầu, sau đó cache ra đĩa. Lần sau phát lại lấy thẳng từ cache; trình duyệt cũng cache
1 năm. Nếu tạo âm thanh thất bại (mất mạng...), view trả 503 và JavaScript tự chuyển sang giọng
đọc có sẵn của trình duyệt (Web Speech API).
"""

import asyncio
import hashlib
import logging
import os
import re
import uuid

from django.conf import settings

logger = logging.getLogger(__name__)

# Tên ngắn → giọng Microsoft. Chỉ cho phép các giọng trong danh sách này.
VOICES = {
    'ava': ('en-US-AvaNeural', 'Ava — nữ, Mỹ, ấm và rõ'),
    'emma': ('en-US-EmmaNeural', 'Emma — nữ, Mỹ, vui vẻ'),
    'jenny': ('en-US-JennyNeural', 'Jenny — nữ, Mỹ, nhẹ nhàng'),
    'andrew': ('en-US-AndrewNeural', 'Andrew — nam, Mỹ, ấm'),
    'brian': ('en-US-BrianNeural', 'Brian — nam, Mỹ, thân thiện'),
    'guy': ('en-US-GuyNeural', 'Guy — nam, Mỹ, rõ ràng'),
    'sonia': ('en-GB-SoniaNeural', 'Sonia — nữ, Anh'),
    'ryan': ('en-GB-RyanNeural', 'Ryan — nam, Anh'),
}

# Tốc độ đọc. "slow" dùng cho shadowing / nghe từ mới.
SPEEDS = {
    'slower': ('-35%', 'Rất chậm'),
    'slow': ('-20%', 'Chậm'),
    'normal': ('+0%', 'Bình thường'),
    'fast': ('+20%', 'Nhanh (tốc độ thật)'),
}

DEFAULT_VOICE = 'ava'
DEFAULT_SPEED = 'normal'
MAX_CHARS = 1500
TIMEOUT_SECONDS = 25


class TTSError(Exception):
    pass


def clean_text(text):
    return re.sub(r'\s+', ' ', text or '').strip()


def cache_path(text, voice, speed):
    key = hashlib.sha1(f'{voice}|{speed}|{text}'.encode('utf-8')).hexdigest()
    return settings.TTS_CACHE_DIR / key[:2] / f'{key}.mp3'


async def _synthesize(text, voice_name, rate, target):
    import edge_tts  # import muộn để test và lệnh khác không cần thư viện này

    communicate = edge_tts.Communicate(text, voice_name, rate=rate)
    await asyncio.wait_for(communicate.save(str(target)), timeout=TIMEOUT_SECONDS)


def get_audio(text, voice=DEFAULT_VOICE, speed=DEFAULT_SPEED):
    """Trả về đường dẫn file mp3 (tạo mới nếu chưa có trong cache)."""
    text = clean_text(text)
    if not text or len(text) > MAX_CHARS:
        raise ValueError('text')
    if voice not in VOICES or speed not in SPEEDS:
        raise ValueError('voice/speed')

    path = cache_path(text, voice, speed)
    if path.exists() and path.stat().st_size > 0:
        return path

    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f'{path.stem}.{uuid.uuid4().hex}.tmp')
    try:
        asyncio.run(_synthesize(text, VOICES[voice][0], SPEEDS[speed][0], tmp))
        if not tmp.exists() or tmp.stat().st_size == 0:
            raise TTSError('empty audio')
        os.replace(tmp, path)
    except Exception as exc:
        logger.warning('TTS failed (%s, %s): %s', voice, speed, exc)
        raise TTSError(str(exc)) from exc
    finally:
        if tmp.exists():
            tmp.unlink(missing_ok=True)
    return path
