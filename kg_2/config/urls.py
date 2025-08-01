"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from contest import views
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from poster import views as poster_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contest/', include('contest.urls', namespace='contest')),
    path('', include('home.urls')),
    path(
        'about/', 
        TemplateView.as_view(template_name='home/about.html'), 
        name='about'
    ),
    path('freeboard/', include('freeboard.urls')),  # 자유게시판
    path('poster/', include('poster.urls')),  #공모전
    path('mypage/', include('mypage.urls')),  #마이페이지
    path('account/', include('account.urls')),  #계정 관련(로그인, 회원가입)
]

# 개발 환경에서만 media 파일 서빙 (이미지, pdf, 등)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
