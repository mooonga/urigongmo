from django.shortcuts import render
from poster.models import Poster
from freeboard.models import Post
from datetime import datetime, timedelta

# Create your views here.

def main_page(request):
    today = datetime.today().date()
    highlight = Poster.objects.order_by('-prize').first()
    new_posters = Poster.objects.order_by('-created_at')[:6]
    hot_posters = Poster.objects.order_by('-views')[:6]
    closing_soon = Poster.objects.filter(end_date__range=[today, today + timedelta(days=3)])
    freeboard_posts = Post.objects.order_by('-created_at')[:5]

    context = {
        'highlight': highlight,
        'new_posters': new_posters,
        'hot_posters': hot_posters,
        'closing_soon': closing_soon,
        'freeboard_posts': freeboard_posts,
    }
    return render(request, 'home/main.html', context)