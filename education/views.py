from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from education.models import Section, Material

from rest_framework.viewsets import ModelViewSet

from education.serializers import SectionSerializer, MaterialSerializer


class SectionViewSet(ModelViewSet):
    """Viewset for Section"""
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

    def perform_create(self, serializer):
        section = serializer.save()
        section.owner = self.request.user
        section.save()


class MaterialCreateApiView(CreateAPIView):
    """Create a new lesson"""
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

    def perform_create(self, serializer):
        material = serializer.save()
        material.owner = self.request.user
        material.save()


class MaterialListApiView(ListAPIView):
    """List of Materials"""
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class MaterialRetrieveApiView(RetrieveAPIView):
    """Get one Material"""
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class MaterialUpdateApiView(UpdateAPIView):
    """Update Material"""
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class MaterialDestroyApiView(DestroyAPIView):
    """Delete Material"""
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
