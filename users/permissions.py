from rest_framework.permissions import BasePermission


class IsOwnerSection(BasePermission):
    """Владельцы раздела."""
    def has_object_permission(self, request, view, obj):
        if obj.section.owner == request.user or request.user.is_superuser:
            return True

        return False


class IsOwnerTest(BasePermission):
    """Владельцы теста."""
    def has_object_permission(self, request, view, obj):
        if obj.test.section.owner == request.user or request.user.is_superuser:
            return True

        return False


class IsOwnerQuestion(BasePermission):
    """Владельцы вопроса."""
    def has_object_permission(self, request, view, obj):
        if obj.question.test.section.owner == request.user or request.user.is_superuser:
            return True

        return False


class IsOwner(BasePermission):
    """Владельцы."""
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user or request.user.is_superuser:
            return True

        return False


class IsTeacher(BasePermission):
    """Преподаватели."""
    def has_permission(self, request, view):
        if request.user.is_teacher or request.user.is_superuser:
            return True

        return False
