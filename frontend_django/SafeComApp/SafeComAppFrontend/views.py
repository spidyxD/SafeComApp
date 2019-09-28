from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.http import Http404
import json
import datetime


# Create your views here.


def home(request):
    """TO HOME PAGE"""
    print("Hola")
    return render(request, "SafeComAppFrontend/index.html", {})

def registrar_persona(request):
    """REGISTRAR PERSONA"""
    print("Registrar Persona")
    return render(request, "SafeComAppFrontend/registrarPersona.html")