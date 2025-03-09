from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericRelation
from .post_models import Post
from .event_models import Event


class Community(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.CharField(default="http://localhost:8000/static/images/community-default.webp", null=True, blank=True)
    
    posts = GenericRelation(Post, related_query_name="community")
    events = GenericRelation(Event, related_query_name="community")
    
    admins = models.ManyToManyField(User, related_name="communities_administered", blank=True)
    members = models.ManyToManyField(User, related_name="communities_joined", blank=True)
    
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="communities_created")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="communities_updated")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name