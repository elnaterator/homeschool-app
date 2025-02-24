from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from .post_models import Post

class Event(models.Model):
    
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    image_url = models.CharField(default="http://localhost:8000/static/images/event-default.webp", null=True, blank=True)
    
    posts = GenericRelation(Post, related_query_name="events")
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="events_created")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="events_updated")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title