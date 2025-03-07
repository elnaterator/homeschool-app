from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="polls_index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="poll_detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="poll_results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="poll_vote"),
]
