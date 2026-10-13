from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hom-nay/', views.today, name='today'),
    path('lo-trinh/', views.roadmap, name='roadmap'),
    path('tuan/<int:number>/', views.week_detail, name='week'),
    path('tuan/<int:number>/on-tap/', views.week_review, name='week_review'),
    path('ngay/<int:number>/', views.day_detail, name='day'),
    path('ngay/<int:number>/luyen-tu/', views.day_practice, name='day_practice'),
    path('on-tap/', views.review, name='review'),
    path('tu-vung/', views.vocab_bank, name='vocab_bank'),
    path('mau-cau/', views.phrase_bank, name='phrases'),
    path('ghi-am/', views.recordings, name='recordings'),
    path('cai-dat/', views.settings_page, name='settings'),
    path('tts/', views.tts_audio, name='tts'),
]
