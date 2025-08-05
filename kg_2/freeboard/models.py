# freeboard/models.py
from django.db import models
from django.conf import settings

class Post(models.Model):
    BOARD_TEAM = 'team'
    BOARD_INFO = 'info'
    BOARD_QNA  = 'qna'
    BOARD_CHOICES = [
        (BOARD_TEAM, '팀원 모집'),
        (BOARD_INFO, '정보 공유'),
        (BOARD_QNA,  '질문 답변'),
    ]

    board      = models.CharField(
        max_length=10,
        choices=BOARD_CHOICES,
        default=BOARD_TEAM,
        help_text="게시판 종류를 선택하세요"
    )
    title      = models.CharField(max_length=200)
    content    = models.TextField()
    author     = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.get_board_display()}] {self.title}"


class Comment(models.Model):
    post       = models.ForeignKey(
        Post, 
        related_name='comments', 
        on_delete=models.CASCADE
    )
    content    = models.TextField()
    author     = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} on {self.post}"
