from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from education.models import Section, Material

from rest_framework.viewsets import ModelViewSet

from education.serializers import SectionSerializer, MaterialSerializer
from users.permissions import IsOwnerSection, IsOwner, IsTeacher


class SectionViewSet(ModelViewSet):
    """Viewset for Section"""
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (IsAdminUser | IsTeacher,)
        elif self.action in ['retrieve', 'list']:
            self.permission_classes = (IsAuthenticated,)
        elif self.action == 'update':
            self.permission_classes = (IsAdminUser | IsOwner,)
        elif self.action == 'destroy':
            self.permission_classes = (IsAdminUser | IsOwner,)
        return super().get_permissions()

    def perform_create(self, serializer):
        section = serializer.save()
        section.owner = self.request.user
        section.save()


class MaterialCreateApiView(CreateAPIView):
    """Create a new Material"""
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = (IsAdminUser | IsOwnerSection,)

    def perform_create(self, serializer):
        material = serializer.save()
        material.owner = self.request.user
        material.save()


class MaterialListApiView(ListAPIView):
    """List of Materials"""
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = (IsAuthenticated,)


class MaterialRetrieveApiView(RetrieveAPIView):
    """Get one Material"""
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = (IsAuthenticated,)


class MaterialUpdateApiView(UpdateAPIView):
    """Update Material"""
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = (IsAdminUser | IsOwner,)


class MaterialDestroyApiView(DestroyAPIView):
    """Delete Material"""
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = (IsAdminUser | IsOwner,)
