# account/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import UserProfile

User = get_user_model()  # 커스텀 User 모델 불러오기

class SignupForm(UserCreationForm):
    nickname = forms.CharField(label='닉네임', max_length=30)
    email = forms.EmailField(label='이메일')

    class Meta:
        model = User
        fields = ('nickname', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='이메일')  # 템플릿상 이메일로 보이게


INTEREST_CHOICES = [
    ('AI', 'AI'),
    ('일러스트', '일러스트'),
    ('디자인', '디자인'),
    ('에세이', '에세이'),
    ('영상', '영상'),
    ('아이디어', '아이디어'),
    ('과학', '과학'),
    ('문화', '문화'),
    ('인문학', '인문학'),
    ('문학', '문학'),
    ('창업', '창업'),
    ('기술', '기술'),
]


#profile edit
class UserProfileForm(forms.ModelForm):
    interests = forms.MultipleChoiceField(
        choices=INTEREST_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-group'}),
        required=False,
        label='관심사',
    )

    class Meta:
        model = UserProfile
        fields = ['nickname', 'age', 'region', 'bio', 'interests']
