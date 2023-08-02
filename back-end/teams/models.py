from django.db import models
from django.conf import Settings, settings


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
        blank=False,
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    members = models.ManyToManyField(
        "users.User",
        blank=False,
    )
