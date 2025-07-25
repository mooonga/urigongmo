from django.urls import path
from . import views

app_name = 'poster'

urlpatterns = [
    path('', views.poster_list, name='poster_list'),
    path('<int:pk>/', views.poster_detail, name='poster_detail'),  # ✅ 상세 보기
]