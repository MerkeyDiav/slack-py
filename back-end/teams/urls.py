from django.urls import path
from .views import TeamDetail, TeamList

urlpatterns = [
    path("team-list/", TeamList.as_view(), name="team-list"),
    path("<int:pk>/", TeamDetail.as_view(), name="team-detail"),
]
