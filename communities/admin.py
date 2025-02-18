from django.contrib import admin

# Register your models here.
from .models import Community, CommunityMember, Update, Comment

admin.site.register(Community)
admin.site.register(CommunityMember)
admin.site.register(Update)
admin.site.register(Comment)
