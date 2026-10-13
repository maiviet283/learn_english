from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from learning.sitemaps import DaySitemap, StaticSitemap, WeekSitemap
from learning.views import robots_txt

sitemaps = {
    'static': StaticSitemap,
    'weeks': WeekSitemap,
    'days': DaySitemap,
}

urlpatterns = [
    path('robots.txt', robots_txt),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('', include('learning.urls')),
]
