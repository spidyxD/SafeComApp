from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Person, Vehicle, RecordVisit, Blacklist
from .serializers import PersonSerializer, VehicleSerializer, RecordVisitSerializer, BlacklistSerializer


# Create your views here.

######################################################################################
## PERSONS


@csrf_exempt
def persons_all(request):
    """
    List all persons
    """
    if request.method == 'GET':
        objs = Person.objects.all()
        serializer = PersonSerializer(objs, many=True)
        return JsonResponse(serializer.data, safe=False)


######################################################################################
## VEHICLE


@csrf_exempt
def vehicles_all(request):
    """
    List all vehicles
    """
    if request.method == 'GET':
        objs = Vehicle.objects.all()
        serializer = VehicleSerializer(objs, many=True)
        return JsonResponse(serializer.data, safe=False)

######################################################################################
## VISIT

@csrf_exempt
def recordVisit_all(request):
    """
    List all RecordVisit
    """
    if request.method == 'GET':
        objs = RecordVisit.objects.all()
        serializer = RecordVisitSerializer(objs, many=True)
        return JsonResponse(serializer.data, safe=False)

######################################################################################
## BLACK LIST

@csrf_exempt
def blackList_all(request):
    """
    List all blackList
    """
    if request.method == 'GET':
        objs = Blacklist.objects.all()
        serializer = BlacklistSerializer(objs, many=True)
        return JsonResponse(serializer.data, safe=False)

######################################################################################
## OTHER CLASSES