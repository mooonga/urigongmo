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

# config/urls.py
#from contest import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from poster import views as poster_views
from django.http import HttpResponse


def health(_):
    return HttpResponse("OK", content_type="text/plain")

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('contest/', include('contest.urls', namespace='contest')),
    path('', include(('home.urls', 'home'), namespace='home')),  # 메인페이지 경로
    path('community/', include('community.urls')),
    path('poster/', include(('poster.urls', 'poster'), namespace='poster')),  #공모전
    path('account/', include('account.urls')),
    path('health-check/', health, name='health-check'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
