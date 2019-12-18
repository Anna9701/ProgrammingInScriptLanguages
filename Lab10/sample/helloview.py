from django.shortcuts import render
import datetime


def hello(request):
    today = datetime.datetime.today().strftime('%d, %b %Y')
    return render(request, 'hello.html', {'now': today})
