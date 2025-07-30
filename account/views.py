#account/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .forms import SignupForm, LoginForm
from .models import UserProfile
from .forms import UserProfileForm


User = get_user_model()

class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    authentication_form = LoginForm

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']  # 이메일을 username으로 사용
            user.save()

            # 🔹 UserProfile 자동 생성
            nickname = form.cleaned_data['nickname']
            UserProfile.objects.create(user=user, nickname=nickname)

            login(request, user)
            return redirect('home:index')  # 네임스페이스 반영
    else:
        form = SignupForm()
    return render(request, 'account/signup.html', {'form': form})

#로그아웃 화면 
class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

#닉네임 중복 확인
def check_nickname(request):
    nickname = request.GET.get('nickname')
    exists = UserProfile.objects.filter(nickname=nickname).exists()
    return JsonResponse({
        'exists': exists,
        'message': '이미 존재하는 닉네임입니다.' if exists else '사용가능한 닉네임입니다.'
    })

#이메일 중복 확인
def check_email(request):
    email = request.GET.get('email')
    exists = User.objects.filter(email=email).exists()
    return JsonResponse({
        'exists': exists,
        'message': '이미 가입한 이메일입니다.' if exists else '사용가능한 이메일입니다.'
    })


#프로필 수정용 함수
def profile_view(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'mypage/profile.html', {'profile': profile})


def profile_edit(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account:profile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'mypage/profile_edit.html', {'form': form})