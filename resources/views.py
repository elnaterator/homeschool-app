from django.shortcuts import render
from .utils import html_response
from .models import Resource, Tag
from django.contrib.postgres.search import SearchQuery, SearchRank


# View functions


def index(request):
    return html_response("index", request)


def search_resources(request):
    query = request.GET.get("query")
    resources = search_objects(query, Resource.objects)
    template = "search_results" if resources else "search_placeholder"
    is_empty_search = not resources
    return html_response(template, request, {"resources": resources, "is_empty_search": is_empty_search})


def search_tags(request):
    query = request.GET.get("query")
    tags = search_objects(query, Tag.objects)
    return html_response("search_tag_results", request, {"tags": tags})


# Helpers


def search_objects(query, objects):
    search_query = SearchQuery(query)
    results = (
        objects.annotate(rank=SearchRank("search_text", search_query))
        .filter(search_text=search_query)
        .order_by("-rank")
    )
    return results
