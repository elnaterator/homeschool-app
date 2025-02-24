from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpRequest
from ..models.event_models import Event
from ..utils import html_response


def events(request: HttpRequest):

    if request.method == "GET":
        events = Event.objects.all()
        context = {
            "events": events,
        }
        return html_response("events", request, context)

    elif request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        start_datetime = request.POST.get("start_datetime")
        end_datetime = request.POST.get("end_datetime")
        if name and description:
            new_event = Event.objects.create(
                name=name,
                description=description,
                start_datetime=start_datetime,
                end_datetime=end_datetime,
                created_by=request.user,
            )
            new_event.save()
        else:
            return HttpResponse(status=400, content="Bad Request")

    else:
        return HttpResponse(status=405, content="Method Not Allowed")


def event(request: HttpRequest, event_id: int):

    if request.method == "GET":
        event_id = request.GET.get("event_id")
        event = get_object_or_404(Event, pk=event_id)
        context = {"event": event}
        return html_response("event", request, context)

    elif request.method == "PUT":
        event_id = request.PUT.get("event_id")
        name = request.PUT.get("name")
        description = request.PUT.get("description")
        start_datetime = request.PUT.get("start_datetime")
        end_datetime = request.PUT.get("end_datetime")
        if event_id and (name or description):
            event = get_object_or_404(Event, pk=event_id)
            if name:
                event.name = name
            if description:
                event.description = description
            if start_datetime:
                event.start_datetime = start_datetime
            if end_datetime:
                event.end_datetime = end_datetime
            event.save()
        return html_response("event", request, context)

    elif request.method == "DELETE":
        event_id = request.DELETE.get("event_id")
        if event_id:
            event = get_object_or_404(Event, pk=event_id)
            event.delete()
        return html_response("event", request, context)

    else:
        return HttpResponse(status=405, content="Method Not Allowed")


def event_posts(request: HttpRequest):

    if request.method == "GET":
        event_id = request.GET.get("event_id")
        event = get_object_or_404(Event, pk=event_id)
        posts = event.posts.all()
        context = {
            "event": event,
            "posts": posts,
        }
        return html_response("event_posts", request, context)

    else:
        return HttpResponse(status=405, content="Method Not Allowed")