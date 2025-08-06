from django.db import models
from django.contrib.auth.models import AbstractUser

# 사용자(User) 모델 (공통)
# account/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [('admin', 'Admin'), ('user', 'User'), ('business', 'Business')]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

#계정 프로필
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField(max_length=100, unique=True)
    age = models.IntegerField(null=True, blank=True)
    region = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    interests = models.JSONField(default=list, blank=True)

#사업체 프로필
class BusinessProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='business_profile')
    company_name = models.CharField(max_length=100)
    business_type = models.CharField(max_length=100)
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    approval_status = models.CharField(max_length=10, choices=[
        ('대기중', '대기중'), ('승인', '승인'), ('거절', '거절')
    ])
