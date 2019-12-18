from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import ShoppingRecord, Shop


def index(request):
    records = dict()
    for record in ShoppingRecord.objects.all():
        if not (record.shop.name in records):
            records[record.shop.name] = list()
        records[record.shop.name].append(Record(record.product.name, record.amount, record.price(), record.isBought))
    return render(request, 'list.html', {'records': records})


class ShopRecords:
    records = list()
    shop = str


class Record:
    name = str()
    amount = str()
    price = str()
    isBought = "No"

    def __init__(self, n, a, p, b):
        self.name = n
        self.amount = str(a)
        self.price = str(p)
        if b:
            self.isBought = "Yes"
