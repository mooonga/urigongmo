from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.

# 사용자(User) 모델
User = get_user_model()

#공모전 정보
class Contest(models.Model):
    title = models.CharField(max_length=200)
    agency = models.CharField(max_length=200, blank=True, null=True)  # 주관기관
    category = models.CharField(max_length=100, blank=True, null=True)  # 분야
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to='contest_images/', null=True, blank=True)

    CONTEST_STATUS_CHOICES = [
        ('대기중', '대기중'),
        ('모집중', '모집중'),
        ('심사중', '심사중'),
        ('종료', '종료'),
    ]
    status = models.CharField(
        max_length=20,
        choices=CONTEST_STATUS_CHOICES,
        default='대기중')


    # 평가 기준별 가중치
    weight_idea = models.FloatField(default=0.25)
    weight_creativity = models.FloatField(default=0.25)
    weight_feasibility = models.FloatField(default=0.25)
    weight_completion = models.FloatField(default=0.25)

    def __str__(self):
        return self.title

#사용자 출품작
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

#일반 심사 점수
class Score(models.Model):
    SCORE_TYPE_CHOICES = [('user', '일반심사'), ('business', '사업자심사')]

    judge = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scores')
    entry = models.ForeignKey('Entry', on_delete=models.CASCADE, related_name='scores')
    criteria = models.CharField(max_length=50, choices=[
        ('기획력', '기획력'),
        ('창의성', '창의성'),
        ('실현가능성', '실현가능성'),
        ('완성도', '완성도'),
    ])
    score = models.PositiveIntegerField()
    score_type = models.CharField(max_length=10, choices=SCORE_TYPE_CHOICES, default='user')
    created_at = models.DateTimeField(auto_now_add=True)

class AdminLog(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_logs')
    action = models.CharField(max_length=100)
    target_type = models.CharField(max_length=50)
    target_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

# 사용자의 찜 목록 관리
class ContestLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='likes')
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, related_name='liked_by')
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'contest')  # 중복 방지

    def __str__(self):
        return f"{self.user.username} likes {self.contest.title}"
    


# 저장한 공모전 모델
class SavedContest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'contest')  # 같은 공모전 중복 저장 방지

    def __str__(self):
        return f"{self.user.username} saved {self.contest.title}"