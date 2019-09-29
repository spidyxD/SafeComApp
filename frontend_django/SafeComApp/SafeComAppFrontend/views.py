from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.http import Http404
import json
import datetime
import requests

# Create your views here.


def home(request):
    """TO HOME PAGE"""
    # With context, we can send variables to templates
    context = {'title': 'Inicio'}
    return render(request, "SafeComAppFrontend/index.html", context)


def registrar_persona(request):
    """REGISTRAR PERSONA"""
    context = {'title': 'Registro Persona'}
    return render(request, "SafeComAppFrontend/registrarPersona.html", context)


def listar_persona(request):
    """REGISTRAR PERSONA"""
    response = requests.get('http://localhost:8000/api/persons/')
    persons = response.json() #returns a list of dictionaries

    context = {
        'title': 'Personas',
        'persons': persons,
    }

    return render(request, "SafeComAppFrontend/listaPersonas.html", context)
