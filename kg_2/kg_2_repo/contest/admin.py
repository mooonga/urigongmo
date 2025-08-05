from django.contrib import admin
from .models import User, UserProfile, BusinessProfile, Contest, Entry, Score, AdminLog



# Register your models here.

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(BusinessProfile)
admin.site.register(Contest)
admin.site.register(Entry)
admin.site.register(Score)
admin.site.register(AdminLog)
