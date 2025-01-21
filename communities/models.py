from django.db import models


# Create your models here.
class Community(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.CharField(default="http://localhost:8000/static/images/community-default.webp", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
