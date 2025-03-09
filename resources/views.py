from django.shortcuts import render
from .utils import html_response
from .models import Resource
from django.contrib.postgres.search import SearchQuery, SearchRank

def search_resources(query):
    search_query = SearchQuery(query)
    results = Resource.objects.annotate(
        rank=SearchRank('search_text', search_query)
    ).filter(search_text=search_query).order_by('-rank')
    return results

# Create your views here.
def index(request):
    return html_response("index", request)

def search(request):
    query = request.GET.get("query")
    resources = search_resources(query)
    return html_response("search_results", request, {"resources": resources})