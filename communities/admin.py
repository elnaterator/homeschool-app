from django.contrib import admin

# Register your models here.
from .models.community_models import Community
from .models.post_models import Post, Comment
from .models.event_models import Event

admin.site.register(Community)
admin.site.register(Event)
admin.site.register(Post)
admin.site.register(Comment)
