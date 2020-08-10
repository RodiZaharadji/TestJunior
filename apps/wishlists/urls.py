from django.urls import path, include
from rest_framework import routers

from apps.wishlists.views import WishListViewSet, ProductToWitchListView

router = routers.DefaultRouter()
router.register(r'', WishListViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('product_to_wishlist/<int:wishlist_id>/<int:product_id>', ProductToWitchListView.as_view()),
]
