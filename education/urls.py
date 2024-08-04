from django.urls import path
from rest_framework.routers import DefaultRouter

from education.apps import EducationConfig
from education.views import SectionViewSet, MaterialListApiView, MaterialRetrieveApiView, MaterialCreateApiView, \
    MaterialUpdateApiView, MaterialDestroyApiView

app_name = EducationConfig.name

router = DefaultRouter()
router.register(r'sections', SectionViewSet, basename='sections')

urlpatterns = [
    path("materials/", MaterialListApiView.as_view(), name="materials_list"),
    path("materials/<int:pk>/", MaterialRetrieveApiView.as_view(), name="materials_retrieve"),
    path("materials/create/", MaterialCreateApiView.as_view(), name="materials_create"),
    path("materials/<int:pk>/update/", MaterialUpdateApiView.as_view(), name="materials_update"),
    path("materials/<int:pk>/delete/", MaterialDestroyApiView.as_view(), name="materials_delete"),
] + router.urls
