from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .forms import SignupForm, LoginForm, UserProfileForm, BusinessProfileForm
from .models import UserProfile, BusinessProfile
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from django.utils.http import url_has_allowed_host_and_scheme
=======
>>>>>>> 7f05855 (비즈니스 계정 분리, 커뮤니티 이미지 업로드)

User = get_user_model()

# 로그인 뷰
class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    authentication_form = LoginForm

    def get_success_url(self):
        redirect_to = self.request.GET.get('next')
        if redirect_to and url_has_allowed_host_and_scheme(redirect_to, self.request.get_host()):
            return redirect_to
        return '/'


# 회원가입 뷰
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']
            user.role = form.cleaned_data['role']
            user.save()

            nickname = form.cleaned_data['nickname']
            UserProfile.objects.create(user=user, nickname=nickname)

            if user.role == 'business':
                BusinessProfile.objects.create(
                    user=user,
                    company_name='미입력',
                    business_type='미입력',
                    contact_email=user.email,
                    phone_number='미입력',
                    approval_status='대기중'
                )

            login(request, user)
            return redirect('home:index')
    else:
        form = SignupForm()
    return render(request, 'account/signup.html', {'form': form})


# 로그아웃 뷰
class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


# 닉네임 중복 확인
def check_nickname(request):
    nickname = request.GET.get('nickname')
    exists = UserProfile.objects.filter(nickname=nickname).exists()
    return JsonResponse({
        'exists': exists,
        'message': '이미 존재하는 닉네임입니다.' if exists else '사용가능한 닉네임입니다.'
    })


# 이메일 중복 확인
def check_email(request):
    email = request.GET.get('email')
    exists = User.objects.filter(email=email).exists()
    return JsonResponse({
        'exists': exists,
        'message': '이미 가입한 이메일입니다.' if exists else '사용가능한 이메일입니다.'
    })


# 마이페이지 프로필 보기
@login_required
def profile_view(request):
    user = request.user
    profile, _ = UserProfile.objects.get_or_create(user=user)

    business_profile = None
    if user.role == 'business':
        business_profile = BusinessProfile.objects.filter(user=user).first()

    context = {
        'profile': profile,
        'business_profile': business_profile,
    }
    return render(request, 'mypage/profile.html', context)


# 마이페이지 프로필 수정
@login_required
def profile_edit(request):
    user = request.user
    form = None
    business_form = None
    profile = None
    business_profile = None

    if user.role == 'business':
        business_profile, _ = BusinessProfile.objects.get_or_create(user=user)
        business_form = BusinessProfileForm(request.POST or None, instance=business_profile)
    else:
        profile, _ = UserProfile.objects.get_or_create(user=user)
        form = UserProfileForm(request.POST or None, instance=profile)

    if request.method == 'POST':
        if (form is None or form.is_valid()) and (business_form is None or business_form.is_valid()):
            if form:
                form.save()
            if business_form:
                business_form.save()
            user.save()
            return redirect('account:profile')

    context = {
        'form': form,
        'business_form': business_form,
        'profile': profile,
        'business_profile': business_profile,
    }
    return render(request, 'mypage/profile_edit.html', context)
