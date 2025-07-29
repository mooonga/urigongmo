from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

class SignUpForm(forms.Form):
    user_type = forms.ChoiceField(
        label='회원 분류',
        choices=[('admin','일반 회원'), ('business','사업체')],
        widget=forms.Select(attrs={'class':'form-select'})
    )
    nickname = forms.CharField(
        label='닉네임',
        max_length=30,
        widget=forms.TextInput(attrs={
            'placeholder':'닉네임 입력',
            'class':'form-control'
        })
    )
    email = forms.EmailField(
        label='이메일',
        widget=forms.EmailInput(attrs={
            'placeholder':'example@domain.com',
            'class':'form-control'
        })
    )
    password1 = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(attrs={
            'placeholder':'8자 이상, 대소문자 혼합',
            'class':'form-control'
        })
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )

    def clean_nickname(self):
        nick = self.cleaned_data['nickname'].strip()
        if User.objects.filter(username=nick).exists():
            raise forms.ValidationError('이미 사용 중인 닉네임입니다.')
        return nick

    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('이미 사용 중인 이메일입니다.')
        return email

    def clean(self):
        cleaned = super().clean()
        pw1 = cleaned.get('password1')
        pw2 = cleaned.get('password2')
        if pw1 and pw2 and pw1 != pw2:
            self.add_error('password2', '비밀번호가 일치하지 않습니다.')
        return cleaned

    def save(self):
        data = self.cleaned_data
        user = User.objects.create_user(
            username    = data['nickname'],
            email       = data['email'],
            password    = data['password1'],
            first_name  = data['nickname'],  # 닉네임 저장 예시
        )
        return user

class EmailLoginForm(forms.Form):
    email = forms.EmailField(
        label=_("이메일"),
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "이메일 입력",
            "autofocus": True,
        })
    )
    password = forms.CharField(
        label=_("비밀번호"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "••••••••",
        }),
    )

    error_messages = {
        "invalid_login": _(
            "이메일 또는 비밀번호가 올바르지 않습니다."
        ),
        "inactive": _("이 계정은 활성화되어 있지 않습니다."),
    }

    def __init__(self, request=None, *args, **kwargs):
        """
        request를 받아두면 authenticate에서 쓸 수 있습니다.
        """
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            # authenticate는 username 인자로 받으므로 email을 넘깁니다
            self.user_cache = authenticate(
                self.request, username=email, password=password
            )
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages["invalid_login"],
                    code="invalid_login",
                )
            else:
                # is_active 체크
                if not self.user_cache.is_active:
                    raise forms.ValidationError(
                        self.error_messages["inactive"],
                        code="inactive",
                    )
        return self.cleaned_data

    def get_user(self):
        return self.user_cache