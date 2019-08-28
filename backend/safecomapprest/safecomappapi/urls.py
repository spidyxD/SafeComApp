from django.urls import path
from . import views


urlpatterns = [
    #####################################
    # PERSON
    path('persons/', views.PersonList.as_view()),
    path('person/create', views.PersonCreate.as_view()),
    path('person/<str:pk>/update', views.PersonUpdate.as_view()),
    path('person/<str:pk>/delete', views.PersonDestroy.as_view()),
    #####################################
    # VEHICLE
    path('vehicles/', views.VehiclesList.as_view()),
    #####################################
    # RECORDVISIT
    path('recordVisits/', views.RecordVisitList.as_view()),
    path('recordVisit/create', views.RecordVisitList.as_view()),
    #####################################
    # BLACKLIST
    path('blackList/', views.BlackList_all.as_view()),
]