from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'poster'

urlpatterns = [
    path('', views.poster_list, name='poster_list'),
    path('<int:pk>/', views.poster_detail, name='poster_detail'),  # ✅ 상세 보기
    path('ongoing/', TemplateView.as_view(template_name='ongoing.html'), name='ongoing'),
    path('closed/', TemplateView.as_view(template_name='closed.html'), name='closed'),
]