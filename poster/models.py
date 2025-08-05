#poster/models.py

from django.db import models

class Poster(models.Model):
    title = models.CharField(max_length=200)  # 공모전 제목
    d_day = models.CharField(max_length=50)   # 디데이 표시
    image = models.ImageField(upload_to='poster_images/')  # 포스터 이미지
    organization = models.CharField(max_length=100)  # 주최
    company_type = models.CharField(max_length=100)  # 기업형태
    target = models.CharField(max_length=100)        # 참여대상
    prize = models.CharField(max_length=100)         # 시상규모
    start_date = models.DateField()                  # 시작일
    end_date = models.DateField()                    # 마감일
    website = models.URLField()                      # 홈페이지 링크
    benefits = models.TextField()                    # 활동혜택
    category = models.CharField(max_length=100)      # 공모분야
    extra = models.TextField(blank=True, null=True)  # 추가혜택
    description = models.TextField()                 # 상세내용
    category_id = models.IntegerField(null=True, blank=True)  #카테고리 id
    created_at = models.DateTimeField(auto_now_add=True)  # 생성일시
    views = models.IntegerField(default=0)   #조회수 저장
    status = models.CharField(
    max_length=20,
    choices=[('진행중', '진행중'), ('마감', '마감')],
    default='진행중'
    )

    def __str__(self):
        return self.title

