from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet

# Create a router
router = DefaultRouter()
# register ViewSets with the router.
router.register('', ServiceViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
