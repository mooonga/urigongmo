# poster/urls.py
from django.urls import path
from . import views

app_name = 'poster'

urlpatterns = [
    # 전체 공모전 목록
    path('', views.poster_list, name='poster_list'),

    # 진행 중인 공모전 목록
    path('ongoing/', views.ongoing_list, name='poster_ongoing'),

    # 종료된 공모전 목록
    path('closed/', views.closed_list, name='poster_closed'),

    # 상세 페이지: /poster/detail/123/ 형식
    path('detail/<int:pk>/', views.poster_detail, name='poster_detail'),
]
