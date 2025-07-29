from django.shortcuts import render


def contest_home(request):
    if not request.user.is_authenticated:
        return render(request, 'contest/permission_denied.html')

    if request.user.role == 'business':
        return redirect('business_contest_list')
    elif request.user.role == 'user':
        return redirect('user_entry_list')
    else:
        return render(request, 'contest/permission_denied.html')
