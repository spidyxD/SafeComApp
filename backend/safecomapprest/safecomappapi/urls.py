from django.urls import path
from . import views


urlpatterns = [
    #####################################
    # PERSON
    path('persons/', views.PersonList.as_view()),
    path('persons/<str:pk>/update', views.PersonUpdate.as_view()),
    #####################################
    # VEHICLE
    path('vehicles/', views.Vehicles_all.as_view()),
    #####################################
    # RECORDVISIT
    path('recordVisit/', views.RecordVisit_all.as_view()),
    #####################################
    # BLACKLIST
    path('blackList/', views.BlackList_all.as_view()),
]