from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'poster'

urlpatterns = [
    path('', views.ongoing_contests, name='poster_ongoing'),
    path('detail/<int:pk>/', views.poster_detail, name='poster_detail'),  # ✅ 상세 보기
    path('ongoing/', views.ongoing_contests, name='poster_ongoing'),  # 진행중인 공모전
    path('closed/', views.closed_contests, name='poster_closed'),     # 마감된 공모전
]