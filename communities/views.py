from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from .models import Community
from django.templatetags.static import static

# Create your views here.
def index(request: HttpRequest):
    communities = Community.objects.all()
    for c in communities:
        c.member_count = c.members.count()
    context = {
        "communities_followed": communities,
        "communities_recommended": communities,
    }
    return html_response("index", request, context)

def communities(request: HttpRequest):
    communities = Community.objects.all()
    for c in communities:
        c.member_count = c.members.count()
    context = {
        "communities_followed": communities,
        "communities_recommended": communities,
    }
    return html_response("communities", request, context)

def updates(request: HttpRequest):
    return render(request, "communities/updates.html")

def events(request: HttpRequest):
    return render(request, "communities/events.html")

def community(request):
    id = request.GET.get("community_id")
    print(id)
    community = Community.get(id)
    context = {
        "community": community,
    }
    template = loader.get_template("communities/community.html")
    return HttpResponse(template.render(context, request))

def html_response(name: str, request: HttpRequest, context: dict = {}) -> HttpResponse:
    ''' 
    Returns a response with partial html template if HX-Request header is set to true, 
    otherwise returns a full html with base template.
    '''
    if request.headers.get("HX-Request") == "true":
        template = loader.get_template(f"communities/{name}_partial.html")
    else:
        template = loader.get_template(f"communities/{name}.html")
    return HttpResponse(template.render(context, request))