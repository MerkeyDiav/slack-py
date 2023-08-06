from django.conf import settings
from django.db import models
from django.urls import reverse
from users.models import User
from teams.models import Team


class Task(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=10000)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="task_creator",
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    team_managing_it = models.OneToOneField(
        Team,
        unique=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    user_assigned = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_task_assigned",
    )
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("task_detail", kwargs={"pk": self.pk})
