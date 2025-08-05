from django.urls import path
from django.views.generic import TemplateView

app_name = 'mypage'

urlpatterns = [
    path('profile/', 
        TemplateView.as_view(template_name='mypage/profile.html'), 
        name='profile'
    ),
    path('saved/', 
        TemplateView.as_view(template_name='mypage/saved.html'), 
        name='saved'
    ),
    path('myposts/', 
        TemplateView.as_view(template_name='mypage/myposts.html'), 
        name='myposts'
    ),
    path('mycomments/', 
        TemplateView.as_view(template_name='mypage/mycomments.html'), 
        name='mycomments'
    ),
]
