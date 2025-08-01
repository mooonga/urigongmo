from django.urls import path
from django.views.generic import TemplateView

app_name = 'account'

urlpatterns = [
    path('login/', 
        TemplateView.as_view(template_name='account/login.html'), 
        name='login'
    ),
    path('signup/', 
        TemplateView.as_view(template_name='account/signup.html'), 
        name='signup'
    ),
]
