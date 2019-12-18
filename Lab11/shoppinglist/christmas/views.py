from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.

from Lab11.shoppinglist.christmas.Record import Record
from .models import ShoppingRecord


def index(request):
    records = dict()
    for record in ShoppingRecord.objects.all():
        if not (record.shop.name in records):
            records[record.shop.name] = list()
        records[record.shop.name].append(
            Record(record.id, record.product.name, record.amount, record.price(), record.isBought))
    return render(request, 'list.html', {'records': records})


def mark_bought(request, record_id):
    record = get_object_or_404(ShoppingRecord, pk=record_id)
    record.isBought = True
    record.save()
    return index(request)
