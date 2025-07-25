# freeboard/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='freeboard_list'),
    path('<int:post_id>/', views.post_detail, name='freeboard_post_detail'),
]