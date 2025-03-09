from django.contrib import admin
from .models import Resource, Provider, Tag

# Register your models here.
admin.site.register(Resource)
admin.site.register(Provider)
admin.site.register(Tag)