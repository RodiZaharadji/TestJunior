from django.urls import path, include
from rest_framework import routers

from apps.products.views import ProductsViewSet

router = routers.DefaultRouter()
router.register(r'', ProductsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
