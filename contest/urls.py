# contest/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # /contest/ → 홈 or 리디렉션
    path('login/', auth_views.LoginView.as_view(template_name='contest/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('upload/', views.upload_entry, name='upload_entry'),
    path('list/', views.contest_list, name='contest_list'),  # ← 추가된 부분
    #path('freeboard/', views.freeboard_list, name='freeboard_list'),
    #path('freeboard/<int:pk>/', views.freeboard_detail, name='freeboard_detail'),
    #path('freeboard/new/', views.freeboard_create, name='freeboard_create'),
]

