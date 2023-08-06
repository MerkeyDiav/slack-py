from django.forms import ModelForm
from tasks.models import Task
from tasks.validators import TaskValidator


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = (
            "title",
            "description",
            "creator",
            "creation_date",
            "team_managing_it",
            "user_assigned",
            "completed",
        )

    def clean(self):
        super().clean()

        # Validate the user_assigned field.
        user_assigned = self.cleaned_data["user_assigned"]
        task = self.cleaned_data["task"]

        if user_assigned is not None:
            TaskValidator().validate_user_assigned(user_assigned, task)

        return self.cleaned_data
