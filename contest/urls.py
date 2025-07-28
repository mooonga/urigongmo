# contest/urls.py

from django.urls import path
from .views import home_views, business_views, user_views
from django.contrib.auth import views as auth_views

app_name = 'contest'

urlpatterns = [
    path('', home_views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='contest/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # 사업자용
    path('register/', business_views.register_contest, name='register_contest'),
    path('contests/', business_views.contest_list, name='contest_list'),

    # 참가자용
    path('upload/', user_views.upload_entry, name='upload_entry'),
    path('entries/', user_views.entry_list, name='entry_list'),
]

