from django.urls import path
from .views.home_views import contest_home
from .views.business_views import (
    register_contest,
    business_contest_list,
    business_score_entry,
)
from .views.user_views import (
    upload_entry,
    entry_list as user_entry_list,
    ongoing_contests,
    closed_contests,
)

app_name = 'contest'

urlpatterns = [
    path('', contest_home, name='contest_home'),

    # 공모전 진행 상태별 보기
    path('ongoing/', ongoing_contests, name='ongoing_contests'),
    path('closed/', closed_contests, name='closed_contests'),

    # 사업자용
    path('business/contest/register/', register_contest, name='register_contest'),
    path('business/contest/list/', business_contest_list, name='business_contest_list'),
    path('business/entry/<int:entry_id>/score/', business_score_entry, name='business_score_entry'),

    # 사용자용
    path('user/entry/upload/', upload_entry, name='upload_entry'),
    path('user/entry/list/', user_entry_list, name='user_entry_list'),
]
