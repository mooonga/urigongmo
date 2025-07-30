from django.contrib import admin
from .models import Contest, Entry, Score, AdminLog
from account.models import UserProfile, BusinessProfile  

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(BusinessProfile)
admin.site.register(Contest)
admin.site.register(Entry)
admin.site.register(Score)
admin.site.register(AdminLog)
