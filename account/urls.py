#account/urls.py
from django.urls import path
from .views import CustomLoginView, signup_view
from home.views import main_page
from . import views
from account.mypage import user_views
from django.contrib.auth.views import LogoutView

app_name = 'account'

urlpatterns = [
    path('', main_page, name='index'), 
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home:index'), name='logout'),
    path('signup/', signup_view, name='signup'),
    path('ajax/check_nickname/', views.check_nickname, name='check_nickname'),
    path('ajax/check_email/', views.check_email, name='check_email'),
    path('mypage/profile/', user_views.profile_view, name='profile'),
    path('mypage/saved/', user_views.saved_view, name='saved'),
    path('mypage/myposts/', user_views.myposts_view, name='myposts'),
    path('mypage/mycomments/', user_views.mycomments_view, name='mycomments'),
    path('mypage/profile/edit/', views.profile_edit, name='profile_edit'),  #수정
]