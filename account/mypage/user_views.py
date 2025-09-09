#account/mypage/user_views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from community.models import Post, Comment, SavedPost

# 1. 프로필 보기
@login_required
def profile_view(request):
    user = request.user
    profile = getattr(user, 'profile', None)
    business_profile = getattr(user, 'business_profile', None)

    return render(request, 'mypage/profile.html', {
        'user': user,
        'profile': profile,
        'business_profile': business_profile,
    })

# 2. 저장한 콘텐츠 보기
@login_required
def saved_view(request):
    #saved_contests = SavedContest.objects.filter(user=request.user)
    saved_posts = SavedPost.objects.filter(user=request.user)

    return render(request, 'mypage/saved.html', {
        #'saved_contests': saved_contests,
        'saved_posts': saved_posts,
    })

# 3. 내가 쓴 게시글
@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'mypage/my_posts.html', {
        'my_posts': posts})

# 4. 내가 단 댓글
@login_required
def my_comments(request):
    comments = Comment.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'mypage/my_comments.html', {
        'my_comments': comments})
