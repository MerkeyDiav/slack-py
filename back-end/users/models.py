from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=("Permissions"),
        related_name="custom_user_permissions",
    )
    groups = models.ManyToManyField(Group, related_name="custom_user_groups")
    created_tasks = models.ManyToManyField(
        "tasks.Task",
        blank=True,
        related_name="task_created_by_user",
        verbose_name=("taches taches créées par le user"),
    )
    created_team = models.ManyToManyField(
        "teams.Team",
        blank=True,
        related_name="teams_created_by_user",
        verbose_name=("Equipes créées par ce user"),
    )
    assigned_task = models.OneToOneField(
        "tasks.Task",
        blank=True,
        unique=True,
        verbose_name=("Taches assignés"),
        on_delete=models.CASCADE,
    )
    joined_team = models.ManyToManyField(
        "teams.Team",
        blank=True,
        verbose_name=("Equipes joins"),
        related_name="teams_user_joined",
    )
