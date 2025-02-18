from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.template import loader
from .models import Community
from django.templatetags.static import static

# Create your views here.
def index(request: HttpRequest):
    communities = Community.objects.all()
    for c in communities:
       update_community_info(c) 
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
    if request.method == "POST":
        # create new update
        pass
    elif request.method == "PUT":
        # update existing update
        pass
    elif request.method == "DELETE":
        # delete existing update
        pass
    elif request.method == "GET":
        if request.GET.get("community_id"):
            # get updates for a specific community
            pass
        elif request.GET.get("update_id"):
            # get a specific update
            pass
        else:
            # get all updates
            pass
    return html_response("updates", request)

def events(request: HttpRequest):
    return html_response("events", request)

def community(request: HttpRequest, community_id: int):
    community = get_object_or_404(Community, pk=community_id)
    update_community_info(community)
    context = {
        "community": community,
    }
    return html_response("community", request, context)

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

def update_community_info(community: Community):
    community.member_count = community.members.count()