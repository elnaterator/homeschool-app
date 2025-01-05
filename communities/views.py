from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Community

# Create your views here.
def index(request):
    # communities = Communities.objects.order_by("-pub_date")[:5]
    template = loader.get_template("communities/index.html")
    context = {
        # "communities": communities,
    }
    return HttpResponse(template.render(context, request))

def communities(request):
    # communities = Community.objects.all()
    template = loader.get_template("communities/communities.html")
    context = {
        # "communities": communities,
    }
    return HttpResponse(template.render(context, request))

def updates(request):
    return render(request, "communities/updates.html")

def events(request):
    return render(request, "communities/events.html")
