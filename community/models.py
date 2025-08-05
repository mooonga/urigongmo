from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    BOARD_CHOICES = [
        ('team', '팀원 모집'),
        ('info', '정보 공유'),
        ('qna', '질문 답변'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # ✅ 수정됨
    board_type = models.CharField(max_length=10, choices=BOARD_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"[{self.get_board_type_display()}] {self.title}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.post.get_board_type_display()}] {self.post.title}"
