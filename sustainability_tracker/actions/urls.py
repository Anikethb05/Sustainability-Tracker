from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SustainabilityActionViewSet

router = DefaultRouter()
router.register(r'actions', SustainabilityActionViewSet, basename='action')

urlpatterns = [
    path('', include(router.urls)),
]
