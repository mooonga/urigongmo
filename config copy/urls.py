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
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from urigongmo.views import (
    signup,
    LoginView,
    UserLogoutView,
    check_email,
    check_nickname,
)

# 더미
dummy = [{
    'image_url': '/static/img/newimg1.png',
    'category': '디자인',
    'category_class': 'design',
    'start_date': '2024.07.01',
    'end_date':   '2024.08.15',
    'title':      '2024 브랜드 아이덴티티 공모전'
}] * 20

contest = {
    'title': '2025 한국콘텐츠진흥원 기획/아이디어 공모전',
    'image_url': '',
    'd_day': 'D-20',
    'host': '문화체육관광부',
    'company': '(주)준콤',
    'company_type': '중소기업',
    'region': '전국',
    'target': '직장인',
    'prize': '639만 원',
    'categories': ['기획/아이디어'],
    'activity_benefits': '인턴 기회 제공',
    'additional_benefits': '우수작 홍보 지원',
    'website': '',
    'start_date': '2025.07.26',
    'end_date': '2025.08.16',
    'description': '기획/아이디어 분야의 창의적인 아이디어를 가진 참가자를 모집합니다.',
    'view_count': 1,
}
profile = {
    'full_name':    '김철수',
    'email':        'kim.chulsoo@example.com',
    'region':       '서울',
    'interests':    ['디자인', 'AI', '기획'],
    'avatar_url':   '/static/img/posterPlaceholder.jpg',
}
saved_contests = [
    {'title': '2025 콘텐츠 아이디어 공모전', 'd_day': 'D-10'},
    {'title': 'AI 서비스 데모 콘테스트', 'd_day': 'D-30'},
]
saved_posts    = [
    {'title': '나만의 웹툰 기획서',   'date': '2025-07-15'},
    {'title': '스마트 농업 솔루션 후기', 'date': '2025-07-10'},
]
my_posts = [
    {'title': '나만의 웹툰 기획서', 'date': '2025-07-20'},
    {'title': '스마트 농업 솔루션 제안', 'date': '2025-07-10'},
]
my_comments = [
    {
        'contest': '콘텐츠 아이디어 공모전',
        'comment': '좋은 기획이네요!',
        'created_at': '2025-07-28 14:35'
    },
    {
        'contest': 'AI 서비스 공모전',
        'comment': '많은 도움이 되었습니다.',
        'created_at': '2025-07-27 09:12'
    },
]
# 진짜 뷰를 만들었을 때 사용할 컨테이너 데이터 삽입 구문
# def ongoing_contests(request):
#     qs = Contest.objects.filter(is_active=True).order_by('-deadline')
#     page = Paginator(qs, 40)
#     page_obj = page.get_page(request.GET.get('page'))
#     return render(request,
#                   'ongoing.html',
#                   {
#                     'contests': page_obj.object_list,
#                     'page_obj': page_obj,
#                     'paginator': page
#                   })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),

    path('accounts/signup/', signup, name='signup'),
    path("accounts/login/", LoginView.as_view(), name="login"),
    path('accounts/logout/', UserLogoutView.as_view(), name='logout'),
    # 중복확인 AJAX
    path('ajax/check_email/', check_email, name='check_email'),
    path('ajax/check_nickname/', check_nickname, name='check_nickname'),
    path('mypage/profile/',
        TemplateView.as_view(
            template_name='mypage/profile.html',
            extra_context={'profile': profile}
        ),
        name='mypage_profile'
    ),
    path(
        'mypage/saved/',
        TemplateView.as_view(
            template_name='mypage/saved.html',
            extra_context={
                'saved_contests': saved_contests,
                'saved_posts':    saved_posts,
            }
        ),
        name='mypage_saved'
    ),
    path(
        'mypage/myposts/',
        TemplateView.as_view(
            template_name='mypage/myposts.html',
            extra_context={'my_posts': my_posts}
        ),
        name='mypage_myposts'
    ),
    path(
        'mypage/mycomments/',
        TemplateView.as_view(
            template_name='mypage/mycomments.html',
            extra_context={'my_comments': my_comments}
        ),
        name='mypage_mycomments'
    ),
    path('ongoing/',
        TemplateView.as_view(
            template_name='ongoing.html',
            extra_context={'contests': dummy}           # ← 여기 추가
        ),
        name='ongoing'
    ),    
    path('closed/', TemplateView.as_view(template_name='closed.html'), name='closed'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('detail/',
        TemplateView.as_view(
            template_name='detail.html',
            extra_context={'contest': contest}
        ),
        name='detail'
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
