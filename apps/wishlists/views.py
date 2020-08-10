from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.wishlists.models import WishList
from apps.wishlists.serializers import WishListSerializer


class WishListViewSet(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer

    def get_queryset(self):
        user = self.request.user

        return WishList.objects.filter(user=user).order_by('pk')

    def create(self, request, *args, **kwargs):
        request.data['user_id'] = request.user.id

        WishList.objects.create(**request.data)

        return Response(request.data)


class ProductToWitchListView(GenericAPIView):

    def post(self, request, wishlist_id, product_id):
        wishlist = request.user.wishlist_set.get(pk=wishlist_id)
        wishlist.products.add(product_id)

        return Response(WishListSerializer(wishlist).data)

    def delete(self, request, wishlist_id, product_id):
        wishlist = request.user.wishlist_set.get(pk=wishlist_id)
        wishlist.products.remove(product_id)

        return Response(WishListSerializer(wishlist).data)


