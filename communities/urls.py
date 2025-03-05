from django.urls import path

from .views import community_views, event_views, post_views

urlpatterns = [
    
    # base url is /communities/
    
    path("", community_views.communities, name="communities"),
    path("<int:community_id>/", community_views.community, name="community"),
    path("<int:community_id>/events", community_views.community_events, name="community_events"),
    path("<int:community_id>/posts", community_views.community_posts, name="community_posts"),
    
    path("events/", event_views.events, name="events"),
    path("events/<int:event_id>/", event_views.event, name="event"),
    path("events/<int:event_id>/posts", event_views.event_posts, name="event_posts"),
    
    path("posts/", post_views.posts, name="posts"),
    path("posts/<int:post_id>/", post_views.post, name="post"),
    path("posts/<int:post_id>/comments", post_views.post_comments, name="post_comments"),
    path("posts/<int:post_id>/comments/<int:comment_id>", post_views.post_comment, name="post_comment"),

]
