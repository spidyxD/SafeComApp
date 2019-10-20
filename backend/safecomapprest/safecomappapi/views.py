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
        -getAllVisitByPerson()-
        -getAllVisitByPlate()-
        getAllVisitByDate()  ** pending      
        -getVehicle()-
        -getBlacklist()-
        -getPerson()-       
    }
"""

######################################################################################
## PERSONS


class PersonList(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonNoExitList(generics.ListAPIView):

    serializer_class = RecordVisitSerializer

    def get_queryset(self):
        """The queryset that should be used for returning objects from this view"""
        query = RecordVisit.objects.filter(outgoing_date__isnull=True)
        return query

    def get_object(self):
        query = self.get_queryset()
        return get_list_or_404(query)



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


class PersonVisits(generics.ListAPIView):
    """getAllVisitByPerson"""
    serializer_class = RecordVisitSerializer
    #lookup_field = "visit_identification"

    def get_queryset(self):
        """The queryset that should be used for returning objects from this view"""
        identification = self.kwargs["pk"]
        #query = RecordVisit.objects.select_related('visit_identification').filter(visit_identification=identification)
        #query = RecordVisit.objects.filter(visit_identification=identification)
        query = RecordVisit.objects.filter(plate__owner__identification=identification)
        return query


    def get_object(self):
        query = self.get_queryset()
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
    serializer_class = VehicleSerializer
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


class VehicleVisits(generics.ListAPIView):
    """getAllVisitByPlate"""
    serializer_class = RecordVisitSerializer
    #lookup_field = "visit_identification"

    def get_queryset(self):
        """The queryset that should be used for returning objects from this view"""
        plate = self.kwargs["pk"]
        query = RecordVisit.objects.select_related('plate').filter(plate=plate)
        #query = RecordVisit.objects.filter(visit_identification=identification)
        return query

    def get_object(self):
        query = self.get_queryset()
        return get_list_or_404(query)


######################################################################################
## RECORD VISIT

##  Here, just GET and POST verbs, we can not DELETE or UPDATE


class RecordVisitList(generics.ListAPIView):
    queryset = RecordVisit.objects.all()
    serializer_class = RecordVisitSerializer


class RecordVisitCreate(generics.ListCreateAPIView):
    queryset = RecordVisit.objects.all()
    serializer_class = RecordVisitSerializer


class RecordVisitUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = RecordVisitSerializer

    def get_object(self):
        visit_id = self.kwargs["pk"]
        return get_object_or_404(RecordVisit, visit_id=visit_id)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class RecordVisitDestroy(generics.DestroyAPIView):
    serializer_class = RecordVisitSerializer

    def get_queryset(self):
        queryset = RecordVisit.objects.filter(visit_id=self.kwargs['pk'])
        return queryset

    def preform_destroy(self, instance):
        serializer = RecordVisitSerializer(data=self.get_queryset())
        serializer.is_valid(True)
        return instance.delete()

######################################################################################
## BLACK LIST


class BlackListList(generics.ListAPIView):
    queryset = Blacklist.objects.all()
    serializer_class = BlacklistSerializer


class BlackListCreate(generics.ListCreateAPIView):
    queryset = Blacklist.objects.all()
    serializer_class = BlacklistSerializer
    #lookup_field = "visitor"

   # def post(self, request, *args, **kwargs):
   #    pass



class BlackListUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = BlacklistSerializer
    lookup_field = "visitor"

    def get_object(self):
        visitor = self.kwargs["visitor"]
        return get_object_or_404(Blacklist, visitor=visitor)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class BlacklistDestroy(generics.DestroyAPIView):
    serializer_class = BlacklistSerializer
    lookup_field = "visitor"

    def get_queryset(self):
        queryset = Blacklist.objects.filter(visitor=self.kwargs['visitor'])
        return queryset

    def preform_destroy(self, instance):
        serializer = BlacklistSerializer(data=self.get_queryset())
        serializer.is_valid(True)
        return instance.delete()

######################################################################################
## OTHER CLASSES

