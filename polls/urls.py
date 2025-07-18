# polls/urls.py

from django.urls import path
from .views import (
    PollListCreateView,
    PollDetailView,
    vote_poll,
    poll_results
)

urlpatterns = [
    # API Polls: list and create
    path('', PollListCreateView.as_view(), name='poll-list-create'),

    # API Polls: retrieve, update, delete specific poll
    path('<int:pk>/', PollDetailView.as_view(), name='poll-detail'),

    # API Polls: submit a vote (one vote per user)
    path('<int:poll_id>/vote/', vote_poll, name='poll-vote'),

    # API Polls: retrieve results for a specific poll
    path('<int:poll_id>/results/', poll_results, name='poll-results'),
]
