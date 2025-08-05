#from django.db import models
#from django.conf import settings  # 여기 추가

#class Post(models.Model):
    #title = models.CharField(max_length=200)
    #content = models.TextField()
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 수정
    #created_at = models.DateTimeField(auto_now_add=True)

#class Comment(models.Model):
    #post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    #content = models.TextField()
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 수정
    #created_at = models.DateTimeField(auto_now_add=True)


# 자유게시판 게시글 저장
#class SavedPost(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #post = models.ForeignKey('freeboard.Post', on_delete=models.CASCADE)
    #saved_at = models.DateTimeField(auto_now_add=True)
