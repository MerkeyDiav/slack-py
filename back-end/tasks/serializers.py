from tasks.models import Task
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ("creator",)
        verbose_name = "Taks serializer"
        verbose_name_plural = "Taks serializers"


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        field = "__all__"
        verbose_name = "task serializer"
        verbose_name_plural = "task serializers"
