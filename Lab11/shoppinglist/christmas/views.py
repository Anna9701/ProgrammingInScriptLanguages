from decimal import Decimal

from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from django.template.defaulttags import register

# Create your views here.

from Lab11.shoppinglist.christmas.Record import Record
from .models import ShoppingRecord, Shop, Product


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def index(request):
    records = dict()
    totals = dict()
    for record in ShoppingRecord.objects.all():
        if not (record.shop.name in records):
            records[record.shop.name] = list()
        records[record.shop.name].append(
            Record(record.id, record.product.name, record.amount, record.price(), record.isBought))
    for key, values in records.items():
        totals[key] = Decimal(0)
        for record in values:
            if not record.isBought:
                totals[key] += Decimal(record.price)

    return render(request, 'list.html', {'records': records, 'totals': totals})


def mark_bought(request, record_id):
    record = get_object_or_404(ShoppingRecord, pk=record_id)
    record.isBought = True
    record.save()
    return redirect('/christmas')


def add_new(request):
    if request.method == "GET":
        return render(request, 'add_new.html', {'form': NewRecordForm()})
    amount = request.POST['amount']
    shop = get_object_or_404(Shop, pk=request.POST['shop'])
    product = get_object_or_404(Product, pk=request.POST['product'])
    record = ShoppingRecord()
    record.shop = shop
    record.product = product
    record.amount = amount
    record.isBought = False
    record.save()
    return redirect('/christmas')


class NewRecordForm(ModelForm):
    class Meta:
        model = ShoppingRecord
        fields = ('product', 'shop', 'amount')
