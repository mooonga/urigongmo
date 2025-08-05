from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.core.paginator import Paginator
from .models import Post, Comment

from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

VALID_BOARDS = {
    'team': '팀원 모집',
    'info': '정보 공유',
    'qna' : '질문 답변',
}

def post_list(request, board):
    if board not in VALID_BOARDS:
        raise Http404("존재하지 않는 커뮤니티 유형입니다.")
    posts     = Post.objects.filter(board=board).order_by('-created_at')
    paginator = Paginator(posts, 10)
    page_obj  = paginator.get_page(request.GET.get('page'))

    return render(request,
        'freeboard/post_list.html',
        {
            'posts'     : page_obj.object_list,
            'page_obj'  : page_obj,
            'paginator' : paginator,
            'board'     : board,
            'board_name': VALID_BOARDS[board],
        }
    )

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('created_at')  # 댓글 목록 불러오기

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('freeboard:post_detail', pk=pk)
    else:
        comment_form = CommentForm()

    return render(request, 'freeboard/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    })

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('freeboard:post_detail', pk=new_post.pk)
    else:
        form = PostForm()
    return render(request, 'freeboard/post_form.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return redirect('freeboard:post_detail', pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('freeboard:post_detail', pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'freeboard/post_form.html', {'form': form})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author == request.user:
        post.delete()
    return redirect('freeboard:freeboard_list')

@login_required
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    post_id = comment.post.pk
    if comment.author == request.user:
        comment.delete()
    return redirect('freeboard:post_detail', pk=post_id)
