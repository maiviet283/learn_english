from datetime import timedelta

from django.conf import settings
from django.http import FileResponse, Http404, HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_GET

from . import content, tts


def _vocab_json(words):
    return [{'word': w['word'], 'ipa': w['ipa'], 'pos': w['pos'], 'vi': w['vi'],
             'ex': w['ex'], 'ex_vi': w['ex_vi'], 'day': w.get('day')} for w in words]


ROUTINE = [
    ('warmup', 'Shadowing', 'Nghe câu ngắn, nói theo ngay', 15),
    ('vocab', 'Từ vựng', 'Thẻ mới + ôn thẻ cũ', 20),
    ('listening', 'Nghe', 'Lần đầu không nhìn lời', 25),
    ('speaking', 'Nói', 'Ghi âm rồi tự nghe lại', 20),
    ('writing', 'Viết', 'Email, tin nhắn, PR…', 10),
]


def _calendar():
    """Lưới 12 tuần × 7 ngày cho heatmap ở trang chủ."""
    days = {d['date']: d['number'] for d in content.all_days()}
    return [
        [{'date': w['start'] + timedelta(days=i), 'day': days.get(w['start'] + timedelta(days=i))}
         for i in range(7)]
        for w in content.all_weeks()
    ]


def home(request):
    today = timezone.localdate()
    day, status = content.scheduled_day(today)
    week = content.get_week(day['week'])
    return render(request, 'learning/home.html', {
        'today': today,
        'days_until_start': (settings.COURSE_START_DATE - today).days,
        'total_days': content.total_days(),
        'day': day,
        'status': status,
        'week': week,
        'phases': content.PHASES,
        'routine': ROUTINE,
        'calendar': _calendar(),
        'day_sections': len(_day_sections(day)),
    })


def roadmap(request):
    weeks = content.all_weeks()
    phases = [(n, info, [w for w in weeks if w['phase'] == n]) for n, info in content.PHASES.items()]
    return render(request, 'learning/roadmap.html', {
        'phases': phases,
        'today': timezone.localdate(),
    })


def week_detail(request, number):
    week = content.get_week(number)
    if not week:
        raise Http404
    return render(request, 'learning/week.html', {
        'week': week,
        'phase': content.PHASES[week['phase']],
        'prev_week': content.get_week(number - 1),
        'next_week': content.get_week(number + 1),
        'today': timezone.localdate(),
    })


def week_review(request, number):
    week = content.get_week(number)
    if not week:
        raise Http404
    sentences = [s for d in week['days'] for s in d['warmup']]
    return render(request, 'learning/week_review.html', {
        'week': week,
        'vocab_json': _vocab_json(content.week_vocab(week)),
        'sentences': sentences,
        'questions': content.week_review_questions(week, 20),
        'quiz_key': f'week-{number}-review',
        'next_week': content.get_week(number + 1),
    })


SECTION_META = [
    ('warmup', 'Khởi động', 'bi-soundwave', 15),
    ('vocab', 'Từ vựng', 'bi-card-text', 20),
    ('lesson', 'Kiến thức', 'bi-lightbulb', None),
    ('listening', 'Nghe', 'bi-headphones', 25),
    ('speaking', 'Nói', 'bi-mic', 20),
    ('reading', 'Đọc', 'bi-book', None),
    ('writing', 'Viết', 'bi-pencil', 10),
    ('quiz', 'Bài tập', 'bi-ui-checks', None),
]


def _day_sections(day):
    present = {'warmup': day['warmup'], 'vocab': True, 'lesson': True, 'listening': day['listening'],
               'speaking': day['speaking'], 'reading': day['reading'], 'writing': day['writing'],
               'quiz': day['quiz']}
    return [{'key': k, 'name': n, 'icon': i, 'mins': m} for k, n, i, m in SECTION_META if present[k]]


def day_detail(request, number):
    day = content.get_day(number)
    if not day:
        raise Http404
    return render(request, 'learning/day.html', {
        'day': day,
        'week': content.get_week(day['week']),
        'prev_day': content.get_day(number - 1),
        'next_day': content.get_day(number + 1),
        'total_days': content.total_days(),
        'vocab_json': _vocab_json([dict(w, day=number) for w in day['vocab']]),
        'key_prefix': f'day-{number}',
        'sections': _day_sections(day),
        'today': timezone.localdate(),
    })


def day_practice(request, number):
    day = content.get_day(number)
    if not day:
        raise Http404
    return render(request, 'learning/practice.html', {
        'day': day,
        'title': f'Ngày {number}: {day["title"]}',
        'back_url': reverse('day', args=[number]),
        'vocab_json': _vocab_json([dict(w, day=number) for w in day['vocab']]),
        'pool_json': _vocab_json(content.week_vocab(content.get_week(day['week']))),
    })


def today(request):
    day, _ = content.scheduled_day(timezone.localdate())
    return redirect('day', number=day['number'])


def review(request):
    """Ôn tập ngắt quãng (kiểu Anki) cho mọi từ đã học."""
    return render(request, 'learning/review.html', {
        'vocab_json': _vocab_json(content.all_vocab()),
    })


def vocab_bank(request):
    return render(request, 'learning/vocab_bank.html', {
        'weeks': content.all_weeks(),
        'total': len(content.all_vocab()),
    })


def phrase_bank(request):
    return render(request, 'learning/phrases.html', {
        'groups': content.all_phrases(),
    })


def recordings(request):
    return render(request, 'learning/recordings.html', {
        'day_titles': {d['number']: d['title'] for d in content.all_days()},
    })


def settings_page(request):
    voices = []
    for key, (voice_id, label) in tts.VOICES.items():
        name, _, desc = label.partition(' — ')
        voices.append({'key': key, 'name': name, 'desc': desc,
                       'flag': 'UK' if voice_id.startswith('en-GB') else 'US'})
    return render(request, 'learning/settings.html', {
        'voices': voices,
        'speeds': tts.SPEEDS,
    })


@require_GET
def tts_audio(request):
    text = tts.clean_text(request.GET.get('t', ''))
    voice = request.GET.get('v', tts.DEFAULT_VOICE)
    speed = request.GET.get('s', tts.DEFAULT_SPEED)
    if not text or len(text) > tts.MAX_CHARS or voice not in tts.VOICES or speed not in tts.SPEEDS:
        return HttpResponseBadRequest('bad tts params')
    try:
        path = tts.get_audio(text, voice, speed)
    except tts.TTSError:
        return HttpResponse('tts unavailable', status=503, content_type='text/plain')
    response = FileResponse(open(path, 'rb'), content_type='audio/mpeg')
    response['Cache-Control'] = 'public, max-age=31536000, immutable'
    return response


def robots_txt(request):
    return HttpResponse(
        f'User-agent: *\nAllow: /\nDisallow: /tts/\n\nSitemap: {settings.SITE_URL}/sitemap.xml\n',
        content_type='text/plain',
    )
