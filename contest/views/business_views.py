from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from contest.models import Contest, Entry, Score
from django.contrib import messages

@login_required
def register_contest(request):
    from contest.forms import ContestForm

    if not request.user.role == 'business':
        return render(request, 'contest/permission_denied.html')

    if request.method == 'POST':
        form = ContestForm(request.POST)
        if form.is_valid():
            contest = form.save(commit=False)
            contest.status = '대기중'
            contest.save()
            return redirect('contest_list')
    else:
        form = ContestForm()

    return render(request, 'contest/register_contest.html', {'form': form})


@login_required
def contest_list(request):
    contests = Contest.objects.all().order_by('-start_date')
    return render(request, 'contest/contest_list.html', {'contests': contests})


# ✅ 사업자 점수 등록 함수 (예시)
@login_required
def business_score_entry(request, entry_id):
    if request.user.role != 'business':
        return render(request, 'contest/permission_denied.html')

    entry = get_object_or_404(Entry, pk=entry_id)

    if request.method == 'POST':
        # 요청으로부터 점수 정보 받기 (예시: form에서)
        criteria_list = ['기획력', '창의성', '실현가능성', '완성도']
        for criteria in criteria_list:
            score_value = int(request.POST.get(criteria, 0))
            Score.objects.create(
                judge=request.user,
                entry=entry,
                criteria=criteria,
                score=score_value,
                score_type='business'  # 핵심 변경
            )
        messages.success(request, "사업자 심사가 완료되었습니다.")
        return redirect('contest_list')

    return render(request, 'contest/business_score_entry.html', {'entry': entry})
