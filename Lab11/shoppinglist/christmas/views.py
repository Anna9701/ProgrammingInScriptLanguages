from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm

# Create your views here.

from Lab11.shoppinglist.christmas.Record import Record
from .models import ShoppingRecord, Shop, Product


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
