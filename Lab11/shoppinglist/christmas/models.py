from django.db import models

# Create your models here.

from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=100)

    def __str__(self):
        return self.name


class ShoppingRecord(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    amount = models.IntegerField()
    isBought = models.BooleanField()

    def __str__(self):
        return str(self.product) + " x " + str(self.amount) + " (" + str(self.shop) + ")"

    def price(self):
        return str(self.product.price * self.amount)
