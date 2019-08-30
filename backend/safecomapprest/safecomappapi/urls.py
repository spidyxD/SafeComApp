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
    path('vehicle/create', views.VehicleCreate.as_view()),
    path('vehicle/<str:pk>/update', views.VehicleUpdate.as_view()),
    path('vehicle/<str:pk>/delete', views.VehicleDestroy.as_view()),
    #####################################
    # RECORDVISIT
    path('recordVisits/', views.RecordVisitList.as_view()),
    path('recordVisit/create', views.RecordVisitCreate.as_view()),
    #####################################
    # BLACKLIST
    path('blackList/', views.BlackListList.as_view()),
    path('blackList/create', views.BlackListCreate.as_view()),
]
