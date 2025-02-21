from django.urls import path, include
from rest_framework.routers import DefaultRouter

from network.apps import NetworkConfig
from network.views import SupplierViewSet

app_name = NetworkConfig.name

router = DefaultRouter()
router.register(r'suppliers', SupplierViewSet, basename='suppliers')


urlpatterns = [
    path('', include(router.urls)),

]