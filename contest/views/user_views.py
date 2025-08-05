from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from contest.models import Entry
from contest.forms import EntryForm
from contest.models import Contest

#출품작 업로드
@login_required
def upload_entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('user_entry_list')
    else:
        form = EntryForm()

    return render(request, 'contest/upload_entry.html', {'form': form})


#출품작 목록 확인
@login_required
def entry_list(request):
    entries = Entry.objects.filter(user=request.user)
    return render(request, 'contest/entry_list.html', {'entries': entries})

#진행 중인 공모전 보기
def ongoing_contests(request):
    contests = Contest.objects.filter(status='진행중').order_by('-start_date')
    return render(request, 'contest/ongoing.html', {'contests': contests})


#종료된 공모전 보기
def closed_contests(request):
    contests = Contest.objects.filter(status='종료').order_by('-end_date')
    return render(request, 'contest/closed.html', {'contests': contests})