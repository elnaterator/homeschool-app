from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Post(models.Model):
    
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="posts_created")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="posts_updated")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="comments_created")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="comments_updated")
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return super().__str__()