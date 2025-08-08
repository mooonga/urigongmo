# poster/views.py
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Poster

PAGE_SIZE = 12

# 정렬 키 매핑 (3개만)
SORT_MAP = {
    "created_desc": "-created_at",  # 최신 등록 순 (기본)
    "end_date_asc": "end_date",     # 마감일 빠른 순
    "end_date_desc": "-end_date",   # 마감일 늦은 순
}

def get_sort_param(request, default_key="created_desc"):
    """요청에서 sort 값을 읽고, 허용되지 않으면 기본값으로 교체"""
    sort = (request.GET.get("sort") or "").strip()
    return sort if sort in SORT_MAP else default_key

def apply_sort(qs, sort_key):
    """정렬 적용 (tie-breaker로 id 내림차 추가)"""
    order_by = SORT_MAP[sort_key]
    return qs.order_by(order_by, "-id")

def paginate_qs(request, qs, page_size=PAGE_SIZE):
    """페이징 객체 생성 후 (page_obj, object_list, paginator) 반환"""
    paginator = Paginator(qs, page_size)
    page_obj = paginator.get_page(request.GET.get("page"))
    return page_obj, page_obj.object_list, paginator
# ---------------------------------------

def ongoing_contests(request):
    today = timezone.now().date()
    qs = Poster.objects.filter(end_date__gte=today)

    # 검색/카테고리 필터
    q = (request.GET.get("q") or "").strip()
    category = (request.GET.get("category") or "").strip()

    if q:
        qs = qs.filter(
            Q(title__icontains=q) |
            Q(organization__icontains=q) |
            Q(description__icontains=q)
        )
    if category:
        qs = qs.filter(category=category)

    # 정렬
    sort_key = get_sort_param(request, default_key="created_desc")
    qs = apply_sort(qs, sort_key)

    # 페이징
    page_obj, posters, paginator = paginate_qs(request, qs, PAGE_SIZE)

    categories = (
        Poster.objects.values_list("category", flat=True).distinct().order_by("category")
    )

    return render(request, "poster/ongoing.html", {
        "posters": posters,
        "page_obj": page_obj,
        "paginator": paginator,
        "query": q,
        "selected_category": category,
        "categories": categories,
        "sort": sort_key,
    })

def closed_contests(request):
    today = timezone.now().date()
    qs = Poster.objects.filter(end_date__lt=today)

    # 검색/카테고리 필터
    q = (request.GET.get("q") or "").strip()
    category = (request.GET.get("category") or "").strip()

    if q:
        qs = qs.filter(
            Q(title__icontains=q) |
            Q(organization__icontains=q) |
            Q(description__icontains=q)
        )
    if category:
        qs = qs.filter(category=category)

    # 정렬
    sort_key = get_sort_param(request, default_key="created_desc")
    qs = apply_sort(qs, sort_key)

    # 페이징
    page_obj, posters, paginator = paginate_qs(request, qs, PAGE_SIZE)

    categories = (
        Poster.objects.values_list("category", flat=True).distinct().order_by("category")
    )

    return render(request, "poster/closed.html", {
        "posters": posters,
        "page_obj": page_obj,
        "paginator": paginator,
        "query": q,
        "selected_category": category,
        "categories": categories,
        "sort": sort_key,
    })

def poster_detail(request, pk):
    poster = get_object_or_404(Poster, pk=pk)
    print("🛠 카테고리:", repr(poster.category))
    poster.views += 1
    poster.save(update_fields=["views"])
    return render(request, "poster/detail.html", {"poster": poster})
