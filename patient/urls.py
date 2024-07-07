from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, UserRegistrationAPIView, activate, UserLoginAPIView, UserLogoutAPIView


# Create a router
router = DefaultRouter()
# register ViewSets with the router.
router.register('list', PatientViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout'),
    path('active/<user_id>/<token>/', activate, name='activate'),
]
