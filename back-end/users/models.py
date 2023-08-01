from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    created_tasks = models.ManyToManyField(
        "tasks.Task",
        verbose_name=("taches taches créées par le user"),
    )
    created_team = models.ManyToManyField(
        "teams.Team",
        verbose_name=("Equipes créées par ce user"),
    )
    assigned_task = models.OneToOneField(
        "tasks.Task",
        verbose_name=("Taches assignés"),
        on_delete=models.CASCADE,
    )
    joined_team = models.ManyToManyField(
        "teams.Team",
        verbose_name=("Equipes joins"),
    )
