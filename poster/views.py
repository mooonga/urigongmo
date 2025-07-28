from django.shortcuts import render, get_object_or_404
from .models import Poster

def poster_list(request):
    posters = Poster.objects.all().order_by('id')
    return render(request, 'poster/poster_list.html', {'posters': posters})

def poster_detail(request, pk):
    poster = get_object_or_404(Poster, pk=pk)
    poster.views += 1  # 조회수 1 증가
    poster.save()      # DB에 저장
    return render(request, 'poster/poster_detail.html', {'poster': poster})
