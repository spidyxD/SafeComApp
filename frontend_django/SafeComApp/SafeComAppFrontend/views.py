from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.http import Http404
import json
import datetime
import requests

# Create your views here.
from .constants import constantsURLs


def home(request):
    """TO HOME PAGE"""
    # With context, we can send variables to templates
    context = {'title': 'Inicio'}
    return render(request, "SafeComAppFrontend/index.html", context)


def nav_registrar_persona(request):
    """REGISTRAR PERSONA"""
    context = {'title': 'Registro Persona'}
    return render(request, "SafeComAppFrontend/registrarPersona.html", context)


def do_registrar_persona(request):
    context = {}

    if request.method == 'POST':

        cedula = request.POST['inputCedula']
        nombre = request.POST['inputName']
        primerApe = request.POST['inputPrimerApe']
        segundoApe = request.POST['inputSegundoApe']

        # Crear diccionario

        toSubmitData = {
            "identification": cedula,
            "name": nombre,
            "first_lastname": primerApe,
            "second_lastname": segundoApe,
        }

        try:
            response = requests.post(constantsURLs.PERSON_CREATE, data=toSubmitData)
            if response.ok:
                context['success'] = "Persona Registrada con éxito"
            else:
                # Clean data
                txt = response.text.replace("[", "").replace("]", "")
                errors = "Persona ya existe" if "already exists" in txt else ""
                context['error'] = f"Algo ha salido mal: {errors}"
        except Exception as e:
            context['error'] = "Ha ocurrido un error"

    context['title'] = "Registro Persona"
    return render(request, 'SafeComAppFrontend/registrarPersona.html', context)


def listar_persona(request):
    """REGISTRAR PERSONA"""
    response = requests.get(constantsURLs.PERSON_LIST)
    persons = response.json()  # returns a list of dictionaries

    context = {
        'title': 'Personas',
        'persons': persons,
    }

    return render(request, "SafeComAppFrontend/listaPersonas.html", context)


def editar_persona(request):
    context = {}
    context['title'] = "Editar Persona"
    if request.method == 'GET':
        identification = request.GET.get('identification')
        if not identification:
            return redirect(listar_persona)
        else:
            # Get the object
            req = "{}{}".format(constantsURLs.PERSON_GET, identification)
            response = requests.get(req)
            if response.ok:
                person = json.loads(response.text)
                context['person'] = person
                return render(request, 'SafeComAppFrontend/editarPersona.html', context)
            else:
                context['error'] = "Ha ocurrido un error con cedula {}".format(identification)
                return render(request, 'SafeComAppFrontend/editarPersona.html', context)

    return redirect(listar_persona)


def do_actualizar_persona(request):

    context = {}

    if request.method == 'POST':

        cedula = request.POST['inputCedula']
        nombre = request.POST['inputName']
        primerApe = request.POST['inputPrimerApe']
        segundoApe = request.POST['inputSegundoApe']

        # Crear diccionario

        toSubmitData = {
            "identification": cedula,
            "name": nombre,
            "first_lastname": primerApe,
            "second_lastname": segundoApe,
        }

        try:
            urlput = '{}{}'.format(constantsURLs.PERSON_UPDATE, cedula)
            response = requests.put(urlput, data=toSubmitData)
            if response.ok:
                context['success'] = "Persona Actualizada con éxito"
                context['person'] = toSubmitData
                return render(request, 'SafeComAppFrontend/editarPersona.html', context)
            else:
                # Clean data
                txt = response.text.replace("[", "").replace("]", "")
                errors = "Persona ya existe" if "already exists" in txt else ""
                context['error'] = f"Algo ha salido mal: {errors}"
        except Exception as e:
            context['error'] = "Ha ocurrido un error"

        return redirect(listar_persona)


def borrar_persona(request):
    context = {}
    context['title'] = "Borrar Persona"
    if request.method == 'GET':
        identification = request.GET.get('identification')
        if not identification:
            return redirect(listar_persona)
        else:
            # Get the object
            req = "{}{}".format(constantsURLs.PERSON_GET, identification)
            response = requests.get(req)
            if response.ok:
                person = json.loads(response.text)
                context['person'] = person
                return render(request, 'SafeComAppFrontend/borrarPersona.html', context)
            else:
                context['error'] = "Ha ocurrido un error con cedula {}".format(identification)
                return render(request, 'SafeComAppFrontend/borrarPersona.html', context)

    return redirect(listar_persona)


def do_borrar_persona(request):

    context = {}

    if request.method == 'POST':

        cedula = request.POST['inputCedula']

        try:
            urldelete = '{}{}'.format(constantsURLs.PERSON_DELETE, cedula)
            response = requests.delete(urldelete)
            if response.ok:
                context['success'] = "Persona borrada con éxito"
                return render(request, 'SafeComAppFrontend/registrarPersona.html', context)
            else:
                # Clean data
                txt = response.text.replace("[", "").replace("]", "")
                errors = "Persona ya existe" if "already exists" in txt else ""
                context['error'] = f"Algo ha salido mal: {errors}"
        except Exception as e:
            context['error'] = "Ha ocurrido un error"

        return redirect(listar_persona)