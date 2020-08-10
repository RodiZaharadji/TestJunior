from rest_framework import serializers

from apps.products.models import Product
from apps.wishlists.models import WishList


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
