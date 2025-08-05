# community/urls.py
from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.community_home, name='community_home'),

    # 게시글 목록 및 작성
    path('<str:board_type>/', views.post_list, name='post_list'),
    path('<str:board_type>/create/', views.post_create, name='post_create'),

    # 게시글 상세, 수정, 삭제
    path('<str:board_type>/<int:pk>/', views.post_detail, name='post_detail'),
    path('<str:board_type>/<int:pk>/edit/', views.post_edit, name='post_edit'),       # 🔹 게시글 수정
    path('<str:board_type>/<int:pk>/delete/', views.post_delete, name='post_delete'), # 🔹 게시글 삭제

    # 댓글 수정, 삭제
    path('comment/<int:pk>/edit/', views.comment_edit, name='comment_edit'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
]
