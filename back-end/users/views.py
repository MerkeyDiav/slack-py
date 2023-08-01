from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions

from .serializers import UserSerializer
from .models import User


# Create your views here.


class UserList(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAdminUser,
    ]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
