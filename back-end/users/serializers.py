from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "firstname",
            "lastname",
        )
        managed = True
        verbose_name = "user serializer"
        verbose_name_plural = "user serializers"
