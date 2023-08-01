from django.urls import path
from django.conf.urls import url
from .views import TaskView

urlpatterns = [
    path("/list", TaskView.as_view()),
]
