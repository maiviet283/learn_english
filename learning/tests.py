import tempfile
from datetime import date, timedelta
from pathlib import Path
from unittest import mock

from django.conf import settings
from django.test import SimpleTestCase, override_settings
from django.utils.html import escape

from . import content, tts


class ContentTests(SimpleTestCase):
    def test_full_roadmap_loaded(self):
        self.assertEqual(len(content.all_weeks()), 12)
        self.assertEqual(content.total_days(), 72)

    def test_every_day_has_all_sections(self):
        for day in content.all_days():
            with self.subTest(day=day['number']):
                self.assertTrue(day['warmup'])
                self.assertGreaterEqual(len(day['vocab']), 10)
                self.assertTrue(day['lesson'])
                self.assertTrue(day['listening'] and day['listening']['questions'])
                self.assertTrue(day['speaking'] and day['speaking']['prompts'])
                self.assertTrue(day['reading'] and day['reading']['questions'])
                self.assertTrue(day['writing'] and day['writing']['task'])
                self.assertTrue(day['quiz'])
                self.assertTrue(day['dictation'])

    def test_vocabulary_is_unique_across_roadmap(self):
        words = [w['word'].lower() for w in content.all_vocab()]
        self.assertEqual(len(words), len(set(words)))

    def test_dates_follow_the_pdf_schedule(self):
        self.assertEqual(content.get_day(1)['date'], settings.COURSE_START_DATE)
        self.assertEqual(content.get_day(7)['date'], settings.COURSE_START_DATE + timedelta(days=7))
        self.assertEqual(content.get_day(72)['date'], settings.COURSE_START_DATE + timedelta(days=82))

    def test_scheduled_day(self):
        start = settings.COURSE_START_DATE
        self.assertEqual(content.scheduled_day(start - timedelta(days=3)), (content.get_day(1), 'before'))
        self.assertEqual(content.scheduled_day(start), (content.get_day(1), 'study'))
        self.assertEqual(content.scheduled_day(start + timedelta(days=8)), (content.get_day(8), 'study'))
        self.assertEqual(content.scheduled_day(start + timedelta(days=6)), (content.get_day(6), 'sunday'))
        self.assertEqual(content.scheduled_day(start + timedelta(days=200)), (content.get_day(72), 'after'))

    def test_bad_question_is_rejected(self):
        with self.assertRaises(content.ContentError):
            content._questions([('Q?', ['a', 'b'], 2, 'x')], 'test')

    def test_split_sentences(self):
        self.assertEqual(content.split_sentences('Hi there. How are you? I am fine.'),
                         ['Hi there.', 'How are you?', 'I am fine.'])


@override_settings(ALLOWED_HOSTS=['testserver'])
class PageTests(SimpleTestCase):
    def test_main_pages(self):
        urls = ['/', '/hom-nay/', '/lo-trinh/', '/on-tap/', '/tu-vung/', '/mau-cau/',
                '/ghi-am/', '/cai-dat/', '/robots.txt', '/sitemap.xml']
        for url in urls:
            with self.subTest(url=url):
                self.assertEqual(self.client.get(url, follow=True).status_code, 200)

    def test_every_day_and_week_renders(self):
        for day in content.all_days():
            with self.subTest(day=day['number']):
                response = self.client.get(f"/ngay/{day['number']}/")
                self.assertContains(response, escape(day["title"]))
                self.assertEqual(self.client.get(f"/ngay/{day['number']}/luyen-tu/").status_code, 200)
        for week in content.all_weeks():
            with self.subTest(week=week['number']):
                self.assertEqual(self.client.get(f"/tuan/{week['number']}/").status_code, 200)
                self.assertEqual(self.client.get(f"/tuan/{week['number']}/on-tap/").status_code, 200)

    def test_unknown_day_is_404(self):
        self.assertEqual(self.client.get('/ngay/0/').status_code, 404)
        self.assertEqual(self.client.get('/ngay/73/').status_code, 404)
        self.assertEqual(self.client.get('/tuan/13/').status_code, 404)

    def test_today_redirects_to_a_day(self):
        response = self.client.get('/hom-nay/')
        self.assertEqual(response.status_code, 302)
        self.assertRegex(response['Location'], r'^/ngay/\d+/$')

    def test_home_before_course_start(self):
        with mock.patch('django.utils.timezone.localdate', return_value=date(2026, 10, 13)):
            response = self.client.get('/')
        self.assertContains(response, 'còn 6 ngày')


@override_settings(ALLOWED_HOSTS=['testserver'])
class TTSViewTests(SimpleTestCase):
    def test_rejects_bad_params(self):
        self.assertEqual(self.client.get('/tts/').status_code, 400)
        self.assertEqual(self.client.get('/tts/', {'t': 'hi', 'v': 'nobody'}).status_code, 400)
        self.assertEqual(self.client.get('/tts/', {'t': 'hi', 's': 'warp'}).status_code, 400)
        self.assertEqual(self.client.get('/tts/', {'t': 'x' * (tts.MAX_CHARS + 1)}).status_code, 400)

    def test_serves_cached_mp3(self):
        with tempfile.TemporaryDirectory() as tmp:
            with override_settings(TTS_CACHE_DIR=Path(tmp)):
                path = tts.cache_path('Hello there', 'ava', 'slow')
                path.parent.mkdir(parents=True)
                path.write_bytes(b'ID3fake-mp3')
                response = self.client.get('/tts/', {'t': '  Hello   there ', 'v': 'ava', 's': 'slow'})
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response['Content-Type'], 'audio/mpeg')
                self.assertIn('immutable', response['Cache-Control'])
                self.assertEqual(b''.join(response.streaming_content), b'ID3fake-mp3')

    def test_returns_503_when_engine_fails(self):
        with mock.patch.object(tts, 'get_audio', side_effect=tts.TTSError('offline')):
            response = self.client.get('/tts/', {'t': 'Hello'})
        self.assertEqual(response.status_code, 503)
