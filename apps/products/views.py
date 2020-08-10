from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from apps.common.permissions import ReadOnly
from apps.products.models import Product
from apps.products.serializers import ProductSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser|ReadOnly]

