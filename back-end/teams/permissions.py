from rest_framework import permissions


class IsCreatorOrTeamMember(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Autoriser l'accès si l'utilisateur est le créateur de la tâche
        if obj.creator == request.user:
            return True

        # Autoriser l'accès si l'utilisateur est membre de la même équipe que le créateur de la tâche
        if request.user.joined_team.filter(
            id__in=obj.creator.joined_team.all()
        ).exists():
            return True

        # Refuser l'accès dans tous les autres cas
        return False


class IsCreator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Autoriser l'accès si l'utilisateur est le créateur de la tâche
        if obj.creator == request.user:
            return True

        # Refuser l'accès dans tous les autres cas
        return False
