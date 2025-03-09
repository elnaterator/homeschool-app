from django.shortcuts import render
from .utils import html_response
from .models import Resource

# Create your views here.
def index(request):
    resources = Resource.objects.all()
    ctx = {
        "resources": resources
    }
    return html_response("index", request, ctx)