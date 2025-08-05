from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from contest.models import Contest, Entry, Score
from contest.forms import ContestForm


@login_required
def register_contest(request):
    if request.user.role != 'business':
        return render(request, 'contest/permission_denied.html')

    if request.method == 'POST':
        form = ContestForm(request.POST)
        if form.is_valid():
            contest = form.save(commit=False)
            contest.status = '대기중'
            contest.save()
            return redirect('business_contest_list')
    else:
        form = ContestForm()

    return render(request, 'contest/register_contest.html', {'form': form})


@login_required
def business_contest_list(request):
    if request.user.role != 'business':
        return render(request, 'contest/permission_denied.html')

    contests = Contest.objects.all().order_by('-start_date')
    return render(request, 'contest/contest_list.html', {'contests': contests})


@login_required
def business_score_entry(request, entry_id):
    if request.user.role != 'business':
        return render(request, 'contest/permission_denied.html')

    entry = get_object_or_404(Entry, pk=entry_id)

    if request.method == 'POST':
        criteria_list = ['기획력', '창의성', '실현가능성', '완성도']
        for criteria in criteria_list:
            score_value = int(request.POST.get(criteria, 0))
            Score.objects.create(
                judge=request.user,
                entry=entry,
                criteria=criteria,
                score=score_value,
                score_type='business'
            )
        messages.success(request, "사업자 심사가 완료되었습니다.")
        return redirect('business_contest_list')

    return render(request, 'contest/business_score_entry.html', {'entry': entry})