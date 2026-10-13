"""
Toàn bộ học liệu của lộ trình 12 tuần.

Mỗi file weekNN.py khai báo một biến WEEK (dict). Để nội dung gọn và dễ sửa, phần lớn dữ liệu
viết dạng tuple; module này chuẩn hóa tuple thành dict, đánh số ngày, tính ngày tháng theo lịch
và kiểm tra lỗi (đáp án nằm ngoài lựa chọn, thiếu trường...) ngay khi import.

Định dạng một ngày (key không bắt buộc ghi chú bằng "tùy chọn"):

    {
        'title': 'Tiêu đề tiếng Việt', 'title_en': 'English title',
        'goal': 'Mục tiêu trong ngày',
        'tasks': ['Hoạt động 1', ...],
        'product': 'Sản phẩm kiểm tra; ngăn cách bằng dấu chấm phẩy',
        'rubric': True,                        # tùy chọn: hiện bảng tự chấm 4 tiêu chí
        'warmup': [(en, vi), ...],             # câu shadowing khởi động
        'vocab': [(word, ipa, pos, vi, example, example_vi), ...],
        'lesson': '<h3>...</h3>',              # HTML kiến thức trọng tâm
        'phrases': [(en, vi), ...],            # tùy chọn: mẫu câu hữu ích
        'listening': {
            'title': ..., 'intro': ...,        # intro tùy chọn
            'speakers': {'A': ('Linh', 'ava'), 'B': ('Tom', 'andrew')},
            'lines': [('A', en, vi), ...],
            'questions': [(question, [options], answer_index, explanation), ...],
            'speed': 'normal',                 # tùy chọn: normal | fast
        },
        'dictation': [en, ...],                # tùy chọn, mặc định tự chọn từ bài nghe
        'speaking': {
            'tips': [...],                     # tùy chọn
            'prompts': [(en, gợi ý vi), ...],
            'model': (en, vi),                 # bài nói mẫu, được tách câu để shadowing
            'seconds': 120,                    # tùy chọn: thời lượng ghi âm gợi ý
        },
        'reading': {
            'title': ..., 'text': [đoạn 1, đoạn 2, ...], 'vi': 'tóm tắt/bản dịch',
            'questions': [...],
        },
        'writing': {'task': ..., 'tips': [...], 'model': en, 'min_words': 50},
        'quiz': [(question, [options], answer_index, explanation[, text_to_speak]), ...],
    }
"""

import random
import re
from datetime import timedelta
from functools import lru_cache

from django.conf import settings

from . import (week01, week02, week03, week04, week05, week06, week07, week08,
               week09, week10, week11, week12)

WEEK_MODULES = [week01, week02, week03, week04, week05, week06, week07, week08,
                week09, week10, week11, week12]

DAYS_PER_WEEK = 6
WEEKDAYS_VI = ['Thứ Hai', 'Thứ Ba', 'Thứ Tư', 'Thứ Năm', 'Thứ Sáu', 'Thứ Bảy', 'Chủ nhật']

PHASES = {
    1: {'name': 'Tháng 1 · Nền tảng', 'focus': 'Ngữ pháp, phát âm và phản xạ nói.',
        'target': 'Nói liền mạch 2–3 phút về chủ đề quen thuộc, không dịch trong đầu từ tiếng Việt.'},
    2: {'name': 'Tháng 2 · Tiếng Anh công việc', 'focus': 'Từ vựng IT, nói trong công việc, viết chuyên nghiệp, đọc tài liệu.',
        'target': 'Hiểu phần lớn một buổi họp dev mà không cần phụ đề.'},
    3: {'name': 'Tháng 3 · Remote & phỏng vấn', 'focus': 'Phỏng vấn, thuyết trình, xử lý tình huống khó.',
        'target': 'Tự tin trong cuộc gọi video và trả lời tốt câu hỏi phỏng vấn kỹ thuật.'},
}

DEFAULT_SPEAKERS = {'A': ('Anna', 'ava'), 'B': ('Ben', 'andrew')}

_SENTENCE_RE = re.compile(r'(?<=[.!?])\s+(?=[A-Z"“\'(])')


class ContentError(ValueError):
    pass


def split_sentences(text):
    return [s.strip() for s in _SENTENCE_RE.split(text.strip()) if s.strip()]


def _pairs(items, where):
    out = []
    for item in items or []:
        if len(item) != 2:
            raise ContentError(f'{where}: cần (en, vi), nhận {item!r}')
        out.append({'en': item[0], 'vi': item[1]})
    return out


def _questions(items, where):
    out = []
    for i, item in enumerate(items or []):
        if len(item) not in (4, 5):
            raise ContentError(f'{where} câu {i + 1}: cần (câu hỏi, lựa chọn, đáp án, giải thích[, đọc])')
        question, options, answer, explain = item[:4]
        if not isinstance(answer, int) or not 0 <= answer < len(options):
            raise ContentError(f'{where} câu {i + 1}: đáp án {answer!r} nằm ngoài lựa chọn')
        if len(set(options)) != len(options):
            raise ContentError(f'{where} câu {i + 1}: lựa chọn bị trùng')
        out.append({
            'q': question, 'options': list(options), 'answer': answer,
            'explain': explain, 'say': item[4] if len(item) == 5 else '',
        })
    return out


def _vocab(items, where):
    out = []
    for i, item in enumerate(items or []):
        if len(item) != 6:
            raise ContentError(f'{where} từ {i + 1}: cần 6 trường, nhận {item!r}')
        word, ipa, pos, vi, ex, ex_vi = item
        out.append({'word': word, 'ipa': ipa, 'pos': pos, 'vi': vi, 'ex': ex, 'ex_vi': ex_vi})
    return out


def _word_count(text):
    return len(re.findall(r"[A-Za-z0-9']+", text))


def _auto_dictation(lines, limit=5):
    """Chọn vài câu vừa độ dài trong bài nghe để chép chính tả, rải đều cả bài."""
    sentences = [s for ln in lines for s in split_sentences(ln['en'])]
    good = [s for s in sentences if 5 <= _word_count(s) <= 16]
    if len(good) <= limit:
        return good
    step = len(good) / limit
    return [good[int(i * step)] for i in range(limit)]


def _normalize_day(raw, number, week, index):
    where = f'Ngày {number}'
    for key in ('title', 'title_en', 'goal', 'tasks', 'product', 'vocab', 'lesson'):
        if not raw.get(key):
            raise ContentError(f'{where}: thiếu "{key}"')

    start = settings.COURSE_START_DATE
    day = {
        'number': number,
        'week': week,
        'index': index,
        'weekday': WEEKDAYS_VI[index],
        'date': start + timedelta(days=(week - 1) * 7 + index),
        'title': raw['title'],
        'title_en': raw['title_en'],
        'goal': raw['goal'],
        'tasks': raw['tasks'],
        'products': [p.strip() for p in raw['product'].split(';') if p.strip()],
        'rubric': raw.get('rubric', False),
        'warmup': _pairs(raw.get('warmup'), f'{where} warmup'),
        'vocab': _vocab(raw['vocab'], where),
        'lesson': raw['lesson'],
        'phrases': _pairs(raw.get('phrases'), f'{where} phrases'),
        'quiz': _questions(raw.get('quiz'), f'{where} quiz'),
        'listening': None,
        'speaking': None,
        'reading': None,
        'writing': raw.get('writing'),
        'dictation': [],
        'dictation_speed': raw.get('dictation_speed', 'normal'),
    }

    lis = raw.get('listening')
    if lis:
        speakers = {k: {'name': v[0], 'voice': v[1]} for k, v in (lis.get('speakers') or DEFAULT_SPEAKERS).items()}
        lines = []
        for item in lis['lines']:
            if len(item) != 3 or item[0] not in speakers:
                raise ContentError(f'{where} listening: dòng sai {item!r}')
            spk = speakers[item[0]]
            lines.append({'speaker': item[0], 'name': spk['name'], 'voice': spk['voice'],
                          'en': item[1], 'vi': item[2]})
        day['listening'] = {
            'title': lis['title'],
            'intro': lis.get('intro', ''),
            'speakers': speakers,
            'lines': lines,
            'speed': lis.get('speed', 'normal'),
            'questions': _questions(lis.get('questions'), f'{where} listening'),
            'words': sum(_word_count(ln['en']) for ln in lines),
        }
        day['dictation'] = raw.get('dictation') or _auto_dictation(lines)
    elif raw.get('dictation'):
        day['dictation'] = raw['dictation']

    spk = raw.get('speaking')
    if spk:
        model_en, model_vi = spk.get('model', ('', ''))
        day['speaking'] = {
            'tips': spk.get('tips', []),
            'prompts': _pairs(spk.get('prompts'), f'{where} speaking'),
            'model_en': model_en,
            'model_vi': model_vi,
            'model_sentences': split_sentences(model_en) if model_en else [],
            'seconds': spk.get('seconds', 120),
        }

    rd = raw.get('reading')
    if rd:
        day['reading'] = {
            'title': rd['title'],
            'text': rd['text'],
            'vi': rd.get('vi', ''),
            'questions': _questions(rd.get('questions'), f'{where} reading'),
            'words': sum(_word_count(p) for p in rd['text']),
        }

    if day['writing']:
        day['writing'] = {'min_words': 50, 'tips': [], **day['writing']}

    return day


@lru_cache(maxsize=1)
def _load():
    weeks, days = [], []
    for wi, module in enumerate(WEEK_MODULES, start=1):
        raw = module.WEEK
        if len(raw['days']) != DAYS_PER_WEEK:
            raise ContentError(f'Tuần {wi}: cần {DAYS_PER_WEEK} ngày, có {len(raw["days"])}')
        week_days = []
        for i, raw_day in enumerate(raw['days']):
            number = (wi - 1) * DAYS_PER_WEEK + i + 1
            day = _normalize_day(raw_day, number, wi, i)
            week_days.append(day)
            days.append(day)
        start = settings.COURSE_START_DATE + timedelta(days=(wi - 1) * 7)
        weeks.append({
            'number': wi,
            'title': raw['title'],
            'title_en': raw['title_en'],
            'goal': raw['goal'],
            'phase': (wi - 1) // 4 + 1,
            'start': start,
            'end': start + timedelta(days=DAYS_PER_WEEK - 1),
            'sunday': start + timedelta(days=6),
            'days': week_days,
        })
    return weeks, days


def all_weeks():
    return _load()[0]


def all_days():
    return _load()[1]


def get_week(number):
    weeks = all_weeks()
    return weeks[number - 1] if 1 <= number <= len(weeks) else None


def get_day(number):
    days = all_days()
    return days[number - 1] if 1 <= number <= len(days) else None


def total_days():
    return len(all_days())


def scheduled_day(today):
    """Ngày học theo lịch của hôm nay.

    Trả về (day, trạng thái): 'before' trước khi bắt đầu, 'study' ngày học, 'sunday' Chủ nhật ôn tập,
    'after' khi đã qua hết lộ trình.
    """
    offset = (today - settings.COURSE_START_DATE).days
    if offset < 0:
        return get_day(1), 'before'
    week_index, weekday = divmod(offset, 7)
    if week_index >= len(all_weeks()):
        return get_day(total_days()), 'after'
    if weekday == 6:
        return get_day((week_index + 1) * DAYS_PER_WEEK), 'sunday'
    return get_day(week_index * DAYS_PER_WEEK + weekday + 1), 'study'


def week_vocab(week):
    return [dict(w, day=d['number']) for d in week['days'] for w in d['vocab']]


def all_vocab():
    return [dict(w, day=d['number'], week=d['week']) for d in all_days() for w in d['vocab']]


def all_phrases():
    """Mẫu câu theo từng ngày (ngày nào có phrases)."""
    return [(d, d['phrases']) for d in all_days() if d['phrases']]


def week_review_questions(week, count=20, seed=None):
    pool = [q for d in week['days'] for q in d['quiz'] if not q['say']]
    rng = random.Random(seed)
    return rng.sample(pool, min(count, len(pool)))
