from django.urls import path
from . import views

urlpatterns = [
    path('persons/', views.persons_all),
    path('vehicles/', views.vehicles_all),
]