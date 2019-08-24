from django.urls import path
from . import views

urlpatterns = [
    #####################################
    # PERSON
    path('persons/', views.persons_all),
    #####################################
    # VEHICLE
    path('vehicles/', views.vehicles_all),
    #####################################
    # RECORDVISIT
    path('recordVisit/', views.recordVisit_all),
    #####################################
    # BLACKLIST
    path('blackList/', views.blackList_all),
]