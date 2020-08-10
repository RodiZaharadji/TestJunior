from rest_framework import serializers

from apps.products.serializers import ProductSerializer
from apps.wishlists.models import WishList


class CustomProductSerializer(ProductSerializer):
    count_of_users = serializers.SerializerMethodField()

    def get_count_of_users(self, obj):
        return len(set(obj.wishlist_set.all().values_list('user')))


class WishListSerializer(serializers.ModelSerializer):
    products = CustomProductSerializer(read_only=True, many=True)

    class Meta:
        model = WishList
        fields = ['id', 'name', 'products']
