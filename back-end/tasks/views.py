from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response

from .permissions import IsCreator, IsCreatorOrTeamMember
from .models import Task
from .serializers import TaskSerializer, TaskListSerializer


class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, IsCreator)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskCreateAPiView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    # def post(self, request):
    #     form = self.get_form(data=request.data)  # type: ignore
    #     if form.is_valid():
    #         task = form.save()
    #         serializer = TaskSerializer(task)
    #         return Response(serializer.data)
    #     else:
    #         return Response(form.errors, status=400)


class TaskListViewSet(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, IsCreatorOrTeamMember)
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
