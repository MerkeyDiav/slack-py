from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
        )
        managed = True
        verbose_name = "user serializer"
        verbose_name_plural = "user serializers"
