from django.shortcuts import render, get_object_or_404
from .models import Poster

def poster_list(request):
    posters = Poster.objects.all().order_by('-created_at')
    return render(request, 'poster/poster_list.html', {'posters': posters})

def poster_detail(request, pk):
    poster = get_object_or_404(Poster, pk=pk)
    return render(request, 'poster/poster_detail.html', {'poster': poster})
