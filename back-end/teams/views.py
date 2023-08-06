from django.shortcuts import render
from rest_framework import generics, permissions

from .serializers import *
from .permissions import *
from .models import Team


class TeamCreateAPIView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TeamCreateSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class TeamListAPIView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, IsCreatorOrTeamMember)
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, IsCreator)
    queryset = Team.objects.all()
    serializer_class = TeamCreateSerializer
