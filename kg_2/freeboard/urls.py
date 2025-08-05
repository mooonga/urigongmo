# freeboard/urls.py

from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = 'freeboard'  # 반드시 있어야 네임스페이스로 url 호출 가능

urlpatterns = [
    path(
        '',
        RedirectView.as_view(
            pattern_name='freeboard:post_list',
            permanent=False,
            query_string=True,
        ),
        {'board': 'team'},    # ← 여기서 기본 board 인자 지정
        name='root_redirect'
    ),
    path('<str:board>/', views.post_list, name='post_list'),
    path('<str:board>/<int:pk>/', views.post_detail, name='post_detail'),
    path('<str:board>/create/',   views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('comment/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
]