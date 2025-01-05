from django.urls import path

from . import views

urlpatterns = [
    # ex: /communities/
    path("", views.index, name="communities_index"),
    path("communities/", views.communities, name="communities_communities"),
    path("updates/", views.updates, name="communities_updates"),
    path("events/", views.events, name="communities_events"),
]
