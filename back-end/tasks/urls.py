from django.urls import path
from .views import TaskList, TaskDetail

urlpatterns = [
    path("list/", TaskList.as_view()),
    path("<int:pk>/", TaskDetail.as_view()),
]
