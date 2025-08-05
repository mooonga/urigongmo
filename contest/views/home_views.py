from django.shortcuts import render, redirect

def contest_home(request):
    #사업체면 등록한 공모전 목록으로 이동
    if request.user.is_authenticated:
        if request.user.role == 'business':
            return redirect('business_contest_list')
        #일반 사용자면 제출한 출품작 목록으로 이동
        elif request.user.role == 'user':
            return redirect('user_entry_list')

    # 로그인 안 했거나 role이 없는 경우
    return render(request, 'contest/public_home.html')