from .views import search_form
from .views import search
from .views import contact
from django.conf.urls import url

urlpatterns = [
    url(r'^search_form/$', search_form),
    url(r'^search/$', search),
    url(r'^contact/$', contact)
]
