from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Lecture
from .forms import ContactForm
from django.core.mail import send_mail


def search_form(request):
    return render(request, 'search_form.html')


def search(request):
    if 'query' in request.GET and request.GET['query']:
        query = request.GET['query']
        lectures = Lecture.objects.filter(name__icontains=query)
        return render(request, 'search_results.html',
                      {'lectures': lectures, 'query': query})
    else:
        return render(request, 'search_form.html',
                      {'error': True})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(cd['subject'], cd['message'], cd['email'], ['noreply@example.com'])
            return HttpResponseRedirect('thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})
