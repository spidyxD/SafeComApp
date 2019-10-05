from django.urls import path
from . import views


urlpatterns = [
    #####################################
    # PERSON
    path('persons/', views.PersonList.as_view()),
    path('persons/noExit', views.PersonNoExitList.as_view()),
    path('person/create', views.PersonCreate.as_view()),
    path('person/<str:pk>/', views.PersonUpdate.as_view()),
    path('person/update/<str:pk>', views.PersonUpdate.as_view()),
    path('person/delete/<str:pk>', views.PersonDestroy.as_view()),
    path('person/visits/<str:pk>', views.PersonVisits.as_view()),
    #####################################
    # VEHICLE
    path('vehicles/', views.VehiclesList.as_view()),
    path('vehicle/create', views.VehicleCreate.as_view()),
    path('vehicle/<str:pk>/', views.VehicleUpdate.as_view()),
    path('vehicle/update/<str:pk>', views.VehicleUpdate.as_view()),
    path('vehicle/delete/<str:pk>', views.VehicleDestroy.as_view()),
    path('vehicle/visits/<str:pk>', views.VehicleVisits.as_view()),
    #####################################
    # RECORDVISIT
    path('recordVisits/', views.RecordVisitList.as_view()),
    path('recordVisit/create', views.RecordVisitCreate.as_view()),
    path('recordVisit/update/<str:pk>', views.RecordVisitCreate.as_view()),
    path('recordVisit/delete/<str:pk>', views.RecordVisitCreate.as_view()),
    #####################################
    # BLACKLIST
    path('blacklist/', views.BlackListList.as_view()),
    path('blacklist/create', views.BlackListCreate.as_view()),
    path('blacklist/<str:visitor>', views.BlackListUpdate.as_view()),
    path('blacklist/update/<str:visitor>', views.BlackListUpdate.as_view()),
    path('blacklist/delete/<str:visitor>', views.BlackListUpdate.as_view()),
]
