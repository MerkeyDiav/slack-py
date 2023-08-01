from .models import Team
from .serializers import TeamSerializer
from django.shortcuts import render
from rest_framework import generics, permissions


class TeamList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
