# freeboard/forms.py

from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):  # 댓글 폼
    class Meta:
        model = Comment
        fields = ['content']