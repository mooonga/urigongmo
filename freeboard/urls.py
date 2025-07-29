# freeboard/urls.py

from django.urls import path
from . import views

app_name = 'freeboard'  # 반드시 있어야 네임스페이스로 url 호출 가능

urlpatterns = [
    path('', views.post_list, name='freeboard_list'),  # 'freeboard_list'로 지정
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('comment/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
]