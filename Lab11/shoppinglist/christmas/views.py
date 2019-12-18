from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import ShoppingRecord, Shop


def index(request):
    records = ShoppingRecord.objects.all()
    shoprecords = ()
    names = [str(record) for record in records]
    prices = [str(record.price) for record in records]
    return render(request, 'list.html', {'names': names, 'prices': prices})


class ShopRecords:
    records = list()
    shop = str


class Record:
    name = str()
    price = str()
