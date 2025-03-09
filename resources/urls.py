from django.urls import path

from . import views

urlpatterns = [
    
    # base url is /resources/
    path("", views.index, name="resource_index"),
    path("search/", views.search, name="resource_search"),
]
