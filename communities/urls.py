from django.urls import path

from . import views

urlpatterns = [
    # ex: /communities/
    path("", views.index, name="communities_index"),
    path("posts/", views.posts, name="communities_posts"),
    path("communities/", views.communities, name="communities_communities"),
    path("events/", views.events, name="communities_events"),
]
