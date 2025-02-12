from django.urls import path, include
from rest_framework.routers import DefaultRouter
from network.views import NetworkElementViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'elements', NetworkElementViewSet, basename='element')
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]
