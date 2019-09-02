from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Person, Vehicle, RecordVisit, Blacklist
from .serializers import PersonSerializer, VehicleSerializer, RecordVisitSerializer, BlacklistSerializer


# Create your views here.
"""
    TODO

    QUERIES: {
        getAllVisitByPerson()
        getAllVisitByPlate()
        getAllVisitByDate()        
        getVehicle()
        getBlacklist()
        getPerson()        
    }
"""

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


class PersonVisits(generics.RetrieveAPIView):
    """getAllVisitByPerson"""
    serializer_class = RecordVisitSerializer
    lookup_field = "visit_identification"

    def get_object(self):
        identification = self.kwargs["pk"]
        #queryset = Book.objects.filter(title__startswith='M')
        query = RecordVisit.objects.filter(visit_identification=identification)
        return get_list_or_404(query)

######################################################################################
## VEHICLE


class VehiclesList(generics.ListAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleCreate(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = PersonSerializer
    lookup_field = "plate"

    def get_object(self):
        plate = self.kwargs["pk"]
        return get_object_or_404(Vehicle, plate=plate)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class VehicleDestroy(generics.DestroyAPIView):
    serializer_class = VehicleSerializer

    def get_queryset(self):
        queryset = Vehicle.objects.filter(identification=self.kwargs['pk'])
        return queryset

    def preform_destroy(self, instance):
        serializer = VehicleSerializer(data=self.get_queryset())
        serializer.is_valid(True)
        return instance.delete()

######################################################################################
## RECORD VISIT

##  Here, just GET and POST verbs, we can not DELETE or UPDATE


class RecordVisitList(generics.ListAPIView):
    queryset = RecordVisit.objects.all()
    serializer_class = RecordVisitSerializer


class RecordVisitCreate(generics.ListCreateAPIView):
    queryset = RecordVisit.objects.all()
    serializer_class = RecordVisitSerializer

######################################################################################
## BLACK LIST


class BlackListList(generics.ListAPIView):
    queryset = Blacklist.objects.all()
    serializer_class = BlacklistSerializer


class BlackListCreate(generics.ListCreateAPIView):
    queryset = Blacklist.objects.all()
    serializer_class = BlacklistSerializer


######################################################################################
## OTHER CLASSES

