from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

# 사용자(User) 모델
class User(AbstractUser):
    ROLE_CHOICES = [('admin', 'Admin'), ('user', 'User'), ('business', 'Business')]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    age = models.IntegerField(null=True, blank=True)
    region = models.CharField(max_length=100, blank=True)

class BusinessProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    business_type = models.CharField(max_length=100)
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    approval_status = models.CharField(max_length=10, choices=[('대기중', '대기중'), ('승인', '승인'), ('거절', '거절')])

class Contest(models.Model):
    title = models.CharField(max_length=200)
    agency = models.CharField(max_length=200, blank=True, null=True)  # 주관기관
    category = models.CharField(max_length=100, blank=True, null=True)  # 분야
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    
    CONTEST_STATUS_CHOICES = [
        ('모집중', '모집중'),
        ('심사중', '심사중'),
        ('종료', '종료'),
    ]
    status = models.CharField(max_length=20, choices=CONTEST_STATUS_CHOICES, default='모집중')

    def __str__(self):
        return self.title

    # 평가 기준별 가중치
    weight_idea = models.FloatField(default=0.25)
    weight_creativity = models.FloatField(default=0.25)
    weight_feasibility = models.FloatField(default=0.25)
    weight_completion = models.FloatField(default=0.25)

    def __str__(self):
        return self.title

class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    category_id = models.IntegerField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)

    # 파일 업로드 필드 추가
    submission_file = models.FileField(upload_to='submissions/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.contest.title}"

class Score(models.Model):
    CRITERIA_CHOICES = [
        ('기획력', '기획력'),
        ('창의성', '창의성'),
        ('실현가능성', '실현가능성'),
        ('완성도', '완성도'),
    ]

    judge = models.ForeignKey(User, on_delete=models.CASCADE, related_name='judge_scores')
    entry = models.ForeignKey('Entry', on_delete=models.CASCADE, related_name='entry_scores')
    score = models.PositiveIntegerField()
    criteria = models.CharField(max_length=50, choices=CRITERIA_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.judge.username} → {self.entry.id} ({self.criteria}: {self.score})"

class BusinessScore(models.Model):
    CRITERIA_CHOICES = [
        ('기획력', '기획력'),
        ('창의성', '창의성'),
        ('실현가능성', '실현가능성'),
        ('완성도', '완성도'),
    ]

    judge_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='business_scores')
    entry = models.ForeignKey('Entry', on_delete=models.CASCADE, related_name='business_entry_scores')
    score = models.PositiveIntegerField()
    criteria = models.CharField(max_length=50, choices=CRITERIA_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[지자체:{self.judge_user.username}] {self.entry.id} - {self.criteria}: {self.score}"

class AdminLog(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_logs')
    action = models.CharField(max_length=100)
    target_type = models.CharField(max_length=50)
    target_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)