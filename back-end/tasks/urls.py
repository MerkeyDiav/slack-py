from django.urls import path
from .views import *

urlpatterns = [
    path("create/", TaskCreateAPiView.as_view(), name="new_task"),
    path("list/", TaskListViewSet.as_view(), name="task_list"),
    path("list/<int:pk>/", TaskDetailAPIView.as_view()),
]
