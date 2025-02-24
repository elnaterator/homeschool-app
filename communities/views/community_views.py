from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpRequest
from ..models.community_models import Community
from ..utils import html_response


def communities(request: HttpRequest):

    if request.method == "GET":
        communities = Community.objects.all()
        for c in communities:
            update_community_info(c)
        context = {
            "communities_followed": communities,
            "communities_recommended": communities,
        }
        return html_response("communities", request, context)

    elif request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        if name and description:
            new_community = Community.objects.create(
                name=name, description=description, created_by=request.user
            )
            new_community.save()
        else:
            return HttpResponse(status=400, content="Bad Request")

    else:
        return HttpResponse(status=405, content="Method Not Allowed")


def community(request: HttpRequest, community_id: int):

    if request.method == "GET":
        community_id = request.GET.get("community_id")
        community = get_object_or_404(Community, pk=community_id)
        context = {"community": community}
        return html_response("community", request, context)

    elif request.method == "PUT":
        community_id = request.PUT.get("community_id")
        name = request.PUT.get("name")
        description = request.PUT.get("description")
        if community_id and (name or description):
            community = get_object_or_404(Community, pk=community_id)
            if name:
                community.name = name
            if description:
                community.description = description
            community.save()
        return html_response("community", request, context)

    elif request.method == "DELETE":
        community_id = request.DELETE.get("community_id")
        if community_id:
            community = get_object_or_404(Community, pk=community_id)
            community.delete()
        return html_response("communities", request, context)

    else:
        return HttpResponse(status=405, content="Method Not Allowed")


def community_events(request: HttpRequest):
    return html_response("events", request)


def community_posts(request: HttpRequest):
    return html_response("posts", request)


#
# Helper functions
#


def update_community_info(community: Community):
    community.member_count = community.members.count()
