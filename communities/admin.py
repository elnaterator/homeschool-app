from django.contrib import admin

# Register your models here.
from .models import Community, CommunityMember

admin.site.register(Community)
admin.site.register(CommunityMember)
