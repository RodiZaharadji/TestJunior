from django.contrib.auth.models import User
from django.db import models

from apps.products.models import Product


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=399)
    products = models.ManyToManyField(Product)
