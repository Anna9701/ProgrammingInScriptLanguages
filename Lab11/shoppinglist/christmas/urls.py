from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:record_id>/', views.mark_bought, name="record_id"),
    path('add_new/', views.add_new),
]