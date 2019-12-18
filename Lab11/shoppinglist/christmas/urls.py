from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="Index"),
    path('<int:record_id>/', views.mark_bought, name="record_id"),
]