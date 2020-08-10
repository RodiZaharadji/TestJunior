from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=399)
    sku = models.CharField(max_length=13)
    price = models.FloatField()
    description = models.TextField()

