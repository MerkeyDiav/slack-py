from django.db import models
from django.conf import settings
from tasks.models import Task
from users.models import User


class Team(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
        max_length=50,
    )
    creation_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=True,
    )
    task_created = models.ManyToManyField(
        Task,
        blank=False,
        null=False,
    )
    creator = models.ForeignKey(
        settings.AUTH,
        on_delete=models.CASCADE,
    )
    members = models.ManyToManyField(
        User,
        blank=False,
        null=False,
    )
