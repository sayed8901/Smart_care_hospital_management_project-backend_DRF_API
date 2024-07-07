from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import DoctorViewSet, SpecializationViewSet, DesignationViewSet, AvailableTimeViewSet, ReviewViewSet


# Create a router
router = DefaultRouter()

# register ViewSets with the router.
router.register('list', DoctorViewSet)
router.register('specialization', SpecializationViewSet)
router.register('designation', DesignationViewSet)
router.register('available_time', AvailableTimeViewSet)
router.register('reviews', ReviewViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
