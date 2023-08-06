from django.core.validators import ValidationError


class TaskValidator(ValidationError):
    def validate_user_assigned(self, user, task):
        if user not in task.team.members.all():
            raise ValidationError(
                "The user can only be assigned to a user in the same team."
            )
