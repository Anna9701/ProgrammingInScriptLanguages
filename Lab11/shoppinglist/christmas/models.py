from django.db import models

# Create your models here.

from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=200)


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=100)


class ShoppingRecord(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    amount = models.IntegerField()
    isBought = models.BooleanField()
