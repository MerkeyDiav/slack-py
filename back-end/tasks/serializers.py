from tasks.models import Task
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "title",
            "description",
            "creator",
            "creation_date",
            "team_managing_it",
            "user_assigned",
        )
        verbose_name = "Taks serializer"
        verbose_name_plural = "Taks serializers"
