from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import Person, Vehicle, RecordVisit, Blacklist
from .serializers import PersonSerializer, VehicleSerializer, RecordVisitSerializer, BlacklistSerializer


# Create your views here.

######################################################################################
## PERSONS

class PersonList(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonCreate(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = PersonSerializer
    lookup_field = "identification"

    def get_object(self):
        identification = self.kwargs["pk"]
        return get_object_or_404(Person, identification=identification)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class PersonDestroy(generics.DestroyAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        queryset = Person.objects.filter(identification=self.kwargs['pk'])
        return queryset

    def preform_destroy(self, instance):
        serializer = PersonSerializer(data=self.get_queryset())
        serializer.is_valid(True)
        return instance.delete()

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