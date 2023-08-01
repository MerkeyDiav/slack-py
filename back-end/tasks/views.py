from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response


from .models import Task
from .serializers import TaskSerializer


class TaskList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
