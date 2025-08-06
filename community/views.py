# community/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, SavedPost
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseRedirect

def community_home(request):
    return render(request, 'community/home.html')

def post_list(request, board_type):
    posts = Post.objects.filter(board_type=board_type).order_by('-created_at')
    query = request.GET.get('q')

    if query:
        posts = posts.filter(title__icontains=query)

    template_name = f'community/{board_type}/post_list.html'
    return render(request, template_name, {
        'posts': posts,
        'board_type': board_type,
    })


@login_required
def post_create(request, board_type):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.board_type = board_type
            post.author = request.user
            post.save()
            return redirect('community:post_list', board_type=board_type)
    else:
        form = PostForm()

    template_name = f'community/{board_type}/post_form.html'
    return render(request, template_name, {
        'form': form,
        'board_type': board_type,
    })

def post_detail(request, board_type, pk):
    post = get_object_or_404(Post, board_type=board_type, pk=pk)

    # 조회수 증가
    post.views += 1
    post.save()
    
    # 댓글 조회
    comments = post.comments.all().order_by('-created_at')

    # 댓글 폼 초기화
    if request.method == 'POST':
        if request.user.is_authenticated:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect('community:post_detail', board_type=board_type, pk=pk)
        else:
            return redirect('account:login')
    else:
        comment_form = CommentForm()

    # 저장 여부 확인 (context에 추가해줘야 함!)
    is_saved = False
    if request.user.is_authenticated:
        is_saved = SavedPost.objects.filter(user=request.user, post=post).exists()

    template_name = f'community/{board_type}/post_detail.html'
    return render(request, template_name, {
        'post': post,
        'board_type': board_type,
        'comments': comments,
        'comment_form': comment_form,
        'is_saved': is_saved,  # ✅ 이거 꼭 추가!
    })


### 게시글 수정
@login_required
def post_edit(request, board_type, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user != post.author:
        return HttpResponseForbidden("수정 권한이 없습니다.")

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('community:post_detail', board_type=board_type, pk=post.pk)
    else:
        form = PostForm(instance=post)

    template_name = f'community/{board_type}/post_form.html'
    return render(request, template_name, {
        'form': form,
        'edit_mode': True,
        'board_type': board_type,
    })

#게시글 삭제
@login_required
def post_delete(request, board_type, pk):
    post = get_object_or_404(Post, pk=pk, board_type=board_type)

    if request.user == post.author:
        post.delete()
        return redirect('community:post_list', board_type=board_type)
    return redirect('community:post_detail', board_type=board_type, pk=pk)

### 댓글 수정
@login_required
def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    board_type = comment.post.board_type

    if request.user != comment.author:
        return redirect('community:post_detail', board_type=board_type, pk=comment.post.pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('community:post_detail', board_type=board_type, pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'community/comment/comment_edit.html', {'form': form})


### 댓글 삭제
@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    board_type = comment.post.board_type
    post_pk = comment.post.pk

    if request.user == comment.author:
        comment.delete()

    return redirect('community:post_detail', board_type=board_type, pk=post_pk)


##게시글 저장
@login_required
def save_post(request, board_type, post_id):
    post = get_object_or_404(Post, board_type=board_type, id=post_id)
    SavedPost.objects.get_or_create(user=request.user, post=post)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


##게시글 취소
@login_required
def unsave_post(request, board_type, post_id):
    post = get_object_or_404(Post, board_type=board_type, id=post_id)
    SavedPost.objects.filter(user=request.user, post=post).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

