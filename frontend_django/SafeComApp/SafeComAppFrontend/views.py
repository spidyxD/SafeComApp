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


##########################################################
# PERSONA VIEW
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
    """LISTAR PERSONAS"""

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


#######################################################################################################################
# VEHICLE VIEW


def nav_registrar_vehiculo(request):
    """REGISTRAR VEHICULO"""
    context = {'title': 'Registro Vehiculo'}
    # SE DEBE ENVIAR LA LISTA DE PERSONAS PARA QUE EL USUARIO ESCOJA LA PERSONA QUE VA EN EL CARRO
    return render(request, "SafeComAppFrontend/registrarVehiculo.html", context)


def do_registrar_vehiculo(request):
    context = {}

    if request.method == 'POST':

        placa = request.POST['inputPlate']
        modelo = request.POST['inputModel']
        marca = request.POST['inputBrand']
        color = request.POST['inputColor']
        propietario = request.POST['inputOwner']

        # Crear diccionario

        toSubmitData = {
            "plate": placa,
            "model": modelo,
            "brand": marca,
            "color": color,
            "owner": propietario

        }

        try:
            response = requests.post(constantsURLs.PERSON_CREATE, data=toSubmitData)
            if response.ok:
                context['success'] = "Vehiculo Registrado con éxito"
            else:
                # Clean data
                txt = response.text.replace("[", "").replace("]", "")
                errors = "Vehiculo ya existe" if "already exists" in txt else ""
                context['error'] = f"Algo ha salido mal: {errors}"
        except Exception as e:
            context['error'] = "Ha ocurrido un error"

    context['title'] = "Registro Vehiculo"
    return render(request, 'SafeComAppFrontend/registrarVehiculo.html', context)


def do_actualizar_vehiculo(request):
    context = {}

    if request.method == 'POST':

        placa = request.POST['inputPlate']
        modelo = request.POST['inputModel']
        marca = request.POST['inputBrand']
        color = request.POST['inputColor']
        propietario = request.POST['inputOwner']

        # Crear diccionario

        toSubmitData = {
            "plate": placa,
            "model": modelo,
            "brand": marca,
            "color": color,
            "owner": propietario
        }

        try:
            urlput = '{}{}'.format(constantsURLs.VEHICLE_UPDATE, placa)
            response = requests.put(urlput, data=toSubmitData)
            if response.ok:
                context['success'] = "Vehiculo Actualizado con éxito"
                context['vehicle'] = toSubmitData
                return render(request, 'SafeComAppFrontend/editarVehiculo.html', context)
            else:
                # Clean data
                txt = response.text.replace("[", "").replace("]", "")
                errors = "Vehiculo ya existe" if "already exists" in txt else ""
                context['error'] = f"Algo ha salido mal: {errors}"
        except Exception as e:
            context['error'] = "Ha ocurrido un error"

        return redirect(listar_vehiculo)


def listar_vehiculo(request):
    """LISTAR VEHICULOS"""
    response = requests.get(constantsURLs.VEHICLE_LIST)
    vehicles = response.json()  # returns a list of dictionaries

    context = {
        'title': 'Vehiculos',
        'vehicles': vehicles,
    }

    return render(request, "SafeComAppFrontend/listaVehiculo.html", context)


def editar_vehiculo(request):

    context = {}
    context['title'] = "Editar Vehiculo"

    if request.method == 'GET':
        plate = request.GET.get('placa')
        if not plate:
            return redirect(listar_vehiculo)
        else:
            # Get the object
            req = "{}{}".format(constantsURLs.VEHICLE_GET, plate)
            response = requests.get(req)
            if response.ok:
                vehicle = json.loads(response.text)
                context['vehicle'] = vehicle
                return render(request, 'SafeComAppFrontend/editarVehiculo.html', context)
            else:
                context['error'] = "Ha ocurrido un error con la placa {}".format(plate)
                return render(request, 'SafeComAppFrontend/editarVehiculo.html', context)

    return redirect(listar_vehiculo)


def borrar_vehiculo(request):

    context = {}
    context['title'] = "Borrar Vehiculo"

    if request.method == 'GET':
        plate = request.GET.get('plate')
        if not plate:
            return redirect(listar_vehiculo)
        else:
            # Get the object
            req = "{}{}".format(constantsURLs.VEHICLE_GET, plate)
            response = requests.get(req)
            if response.ok:
                vehicle = json.loads(response.text)
                context['vehicle'] = vehicle
                return render(request, 'SafeComAppFrontend/borrarVehiculo.html', context)
            else:
                context['error'] = "Ha ocurrido un error con la placa {}".format(plate)
                return render(request, 'SafeComAppFrontend/borrarVehiculo.html', context)

    return redirect(listar_vehiculo)


def do_borrar_vehiculo(request):
    context = {}

    if request.method == 'POST':

        placa = request.POST['inputPlaca']

        try:
            urldelete = '{}{}'.format(constantsURLs.VEHICLE_DELETE, placa)
            response = requests.delete(urldelete)
            if response.ok:
                context['success'] = "Vehiculo borrado con éxito"
                return render(request, 'SafeComAppFrontend/registrarVehiculo.html', context)
            else:
                # Clean data
                txt = response.text.replace("[", "").replace("]", "")
                errors = "Vehiculo ya existe" if "already exists" in txt else ""
                context['error'] = f"Algo ha salido mal: {errors}"
        except Exception as e:
            context['error'] = "Ha ocurrido un error"

        return redirect(listar_vehiculo)


##########################################################
# VISIT VIEW


def nav_registrar_visita(request):
    """REGISTRAR VISITA"""
    context = {'title': 'Registro Visita'}
    # SE DEBE ENVIAR LA LISTA DE VEHICULOS PARA QUE EL USUARIO ESCOJA EL VEHICULO QUE ESTA INGRESANDO
    return render(request, "SafeComAppFrontend/registrarVisita.html", context)


def do_registrar_visita(request):
    context = {}

    if request.method == 'POST':

        fecha_ingreso = request.POST['inputIncomingDate']
        fecha_salida = request.POST['inputOutgoingDate']
        placa = request.POST['inputPlate']
        motivo = request.POST['inputReason']

        # Crear diccionario

        toSubmitData = {
            "incoming_date": fecha_ingreso,
            "outgoing_date": fecha_salida,
            "plate": placa,
            "reason": motivo

        }

        try:
            response = requests.post(constantsURLs.VISIT_CREATE, data=toSubmitData)
            if response.ok:
                context['success'] = "Visita Registrada con éxito"
            else:
                # Clean data
                txt = response.text.replace("[", "").replace("]", "")
                errors = "Visita ya registrada" if "already exists" in txt else ""
                context['error'] = f"Algo ha salido mal: {errors}"
        except Exception as e:
            context['error'] = "Ha ocurrido un error"

    context['title'] = "Registro Visita"
    return render(request, 'SafeComAppFrontend/registrarVisita.html', context)


def do_actualizar_visita(request):
    context = {}

    if request.method == 'POST':

        fecha_ingreso = request.POST['inputIncomingDate']
        fecha_salida = request.POST['inputOutgoingDate']
        placa = request.POST['inputPlate']
        motivo = request.POST['inputReason']

        # Crear diccionario

        toSubmitData = {
            "incoming_date": fecha_ingreso,
            "outgoing_date": fecha_salida,
            "plate": placa,
            "reason": motivo
        }

        try:
            urlput = '{}{}'.format(constantsURLs.VISIT_UPDATE, placa)
            response = requests.put(urlput, data=toSubmitData)
            if response.ok:
                context['success'] = "Visita Actualizada con éxito"
                context['visit'] = toSubmitData
                return render(request, 'SafeComAppFrontend/editarVisita.html', context)
            else:
                # Clean data
                txt = response.text.replace("[", "").replace("]", "")
                errors = "Visita ya existe" if "already exists" in txt else ""
                context['error'] = f"Algo ha salido mal: {errors}"
        except Exception as e:
            context['error'] = "Ha ocurrido un error"

        return redirect(listar_visita)


def listar_visita(request):
    """LISTAR VISITAS"""
    response = requests.get(constantsURLs.VISIT_LIST)
    visits = response.json()  # returns a list of dictionaries

    context = {
        'title': 'Visits',
        'visits': visits,
    }

    return render(request, "SafeComAppFrontend/listaVisitas.html", context)


def editar_visita(request):

    context = {}
    context['title'] = "Editar Visita"

    if request.method == 'GET':
        plate = request.GET.get('placa')
        if not plate:
            return redirect(listar_vehiculo)
        else:
            # Get the object
            req = "{}{}".format(constantsURLs.VISIT_GET, plate)
            response = requests.get(req)
            if response.ok:
                vehicle = json.loads(response.text)
                context['visit'] = vehicle
                return render(request, 'SafeComAppFrontend/editarVisita.html', context)
            else:
                context['error'] = "Ha ocurrido un error con la placa {}".format(plate)
                return render(request, 'SafeComAppFrontend/editarVisita.html', context)

    return redirect(listar_visita)


def borrar_visita(request):

    context = {}
    context['title'] = "Borrar Visita"

    if request.method == 'GET':
        plate = request.GET.get('plate')
        if not plate:
            return redirect(listar_visita)
        else:
            # Get the object
            req = "{}{}".format(constantsURLs.VISIT_GET, plate)
            response = requests.get(req)
            if response.ok:
                vehicle = json.loads(response.text)
                context['visit'] = vehicle
                return render(request, 'SafeComAppFrontend/borrarVisita.html', context)
            else:
                context['error'] = "Ha ocurrido un error con la placa {}".format(plate)
                return render(request, 'SafeComAppFrontend/borrarVisita.html', context)

    return redirect(listar_visita)


def do_borrar_visita(request):
    context = {}

    if request.method == 'POST':

        placa = request.POST['inputPlate']

        try:
            urldelete = '{}{}'.format(constantsURLs.VISIT_DELETE, placa)
            response = requests.delete(urldelete)
            if response.ok:
                context['success'] = "Visita borrada con éxito"
                return render(request, 'SafeComAppFrontend/registrarVisita.html', context)
            else:
                # Clean data
                txt = response.text.replace("[", "").replace("]", "")
                errors = "Visita no ha sido registrada" if "already exists" in txt else ""
                context['error'] = f"Algo ha salido mal: {errors}"
        except Exception as e:
            context['error'] = "Ha ocurrido un error"

        return redirect(listar_visita)


#######################################################################################################################
# Blacklist

def nav_registrar_bloqueo(request):
    """REGISTRAR VISITA"""

    context = {'title': 'Registro Bloqueo'}

    # SE DEBE ENVIAR LA LISTA DE PERSONAS PARA QUE EL USUARIO ESCOJA LA PESONA QUE SE VA A BLOQUEAR
    try:
        response = requests.get(constantsURLs.PERSON_LIST)

        if response.ok:
            persons = response.json()  # returns a list of dictionaries

            context = {
                'persons': persons,
            }

            return render(request, 'SafeComAppFrontend/registrarBloqueo.html', context)

        else:
            context['error'] = f"Algo ha salido mal con la peticion al servidor"

    except Exception as e:
        context['error'] = "Ha ocurrido un error"

    return render(request, "SafeComAppFrontend/registrarBloqueo.html", context)


def do_registrar_bloqueo(request):
    return None


def listar_bloqueo(request):
    return None


def editar_bloqueo(request):
    return None


def do_actualizar_bloqueo(request):
    return None


def borrar_bloqueo(request):
    return None


def do_borrar_bloqueo(request):
    return None
