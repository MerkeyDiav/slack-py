from django.db import models
from django.contrib.auth import authenticate
from django.conf import Settings, settings
from users.models import User


class Team(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
        max_length=50,
    )
    creation_date = models.DateTimeField(
        auto_now_add=True,
    )
    task_created = models.ManyToManyField(
        "tasks.Task",
        blank=True,
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="creator_of_the_team",
    )
    members = models.ManyToManyField(
        "users.User",
        blank=True,
        related_name="members_of_this_team",
    )

    class Meta:
        verbose_name = "team"
        verbose_name_plural = "teams"
