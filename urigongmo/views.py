from django.shortcuts       import render, redirect
from django.contrib         import messages
from django.http            import JsonResponse
from django.contrib.auth    import views as auth_views
from django.contrib.auth.models import User

from .forms import SignUpForm
from django.contrib.auth.views import LoginView as AuthLoginView
from .forms import EmailLoginForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '회원가입이 완료되었습니다. 로그인해 주세요.')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})

class LoginView(auth_views.LoginView):
    template_name = 'account/login.html'
    authentication_form = EmailLoginForm
    redirect_authenticated_user = True

class UserLogoutView(auth_views.LogoutView):
    next_page = 'index'

def check_email(request):
    exists = User.objects.filter(email=request.GET.get('email','').strip()).exists()
    return JsonResponse({'exists': exists})

def check_nickname(request):
    exists = User.objects.filter(username=request.GET.get('nickname','').strip()).exists()
    return JsonResponse({'exists': exists})
