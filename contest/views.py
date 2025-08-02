from django.shortcuts import render, get_object_or_404, redirect
from .forms import EntryForm
from .models import Contest

# Create your views here.

def upload_entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('entry_success')  # 성공 시 이동할 페이지 (추후 추가 가능)
    else:
        form = EntryForm()
    return render(request, 'contest/upload_entry.html', {'form': form})

def entry_success(request):
    return render(request, 'contest/entry_success.html')

def contest_list(request):
    contests = Contest.objects.all()
    return render(request, 'contest/contest_list.html', {'contests': contests})

def home(request):
    return redirect('contest_list')  # 또는 render(request, 'contest/home.html') 로 직접 템플릿 연결 가능