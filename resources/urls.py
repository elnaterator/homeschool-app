from django.urls import path

from . import views

urlpatterns = [
    
    # base url is /resources/
    path("", views.index, name="resource_index"),
    path("search/", views.search_resources, name="resource_search"),
    path("search_tags/", views.search_tags, name="tag_search"),
]
