from django.urls import path

from . import views

urlpatterns = [
    # ex: /communities/
    path("", views.index, name="communities_index")
]
