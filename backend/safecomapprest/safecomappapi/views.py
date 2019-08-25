from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .models import Person, Vehicle, RecordVisit, Blacklist
from .serializers import PersonSerializer, VehicleSerializer, RecordVisitSerializer, BlacklistSerializer


# Create your views here.

######################################################################################
## PERSONS

class Persons_all_objs(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

######################################################################################
## VEHICLE


class Vehicles_all(generics.ListAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

######################################################################################
## VISIT


class RecordVisit_all(generics.ListAPIView):
    queryset = RecordVisit.objects.all()
    serializer_class = RecordVisitSerializer


######################################################################################
## BLACK LIST


class BlackList_all(generics.ListAPIView):
    queryset = Blacklist.objects.all()
    serializer_class = BlacklistSerializer

######################################################################################
## OTHER CLASSES