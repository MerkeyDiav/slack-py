from rest_framework import serializers

from .models import Team


# Ce serializer nommé TeamSerializer permet juste de recuperer les données
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


# Ce serializer est utilisé pour toute les autres methodes: POST, PUT, DELETE
class TeamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        exclude = ("creator",)
