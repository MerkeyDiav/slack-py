from django.urls import path
from .views import *

urlpatterns = [
    path("list/", TeamListAPIView.as_view(), name="team-list"),
    path("list/<int:pk>/", TeamDetailAPIView.as_view(), name="team-detail"),
    path("create/", TeamCreateAPIView.as_view(), name="create-new-team"),
]
