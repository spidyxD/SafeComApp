from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Person
from .serializers import PersonSerializer

# Create your views here.

@csrf_exempt
def persons_all(request):
    """
    List all persons
    """
    if request.method == 'GET':
        snippets = Person.objects.git ()
        serializer = PersonSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)