from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from . import content


class StaticSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1.0
    protocol = 'https'

    def items(self):
        return ['home', 'roadmap', 'vocab_bank', 'phrases']

    def location(self, item):
        return reverse(item)


class WeekSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8
    protocol = 'https'

    def items(self):
        return [w['number'] for w in content.all_weeks()]

    def location(self, number):
        return reverse('week', args=[number])


class DaySitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7
    protocol = 'https'

    def items(self):
        return [d['number'] for d in content.all_days()]

    def location(self, number):
        return reverse('day', args=[number])
