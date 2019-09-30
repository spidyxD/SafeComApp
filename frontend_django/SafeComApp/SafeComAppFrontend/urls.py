from django.urls import path
from . import views


urlpatterns = [
    ##########################################################
    # PERSONA URLS
    path('', views.home, name='index'),
    path('registrarPersona', views.nav_registrar_persona, name="registroPersona"),
    path('doregistrarPersona', views.do_registrar_persona, name="doregistroPersona"),
    path('listarPersona', views.listar_persona, name="listarPersona"),
    path('editarPersona/', views.editar_persona, name="editarPersona"),
    path('doeditarPersona/', views.do_actualizar_persona, name="doeditarPersona"),
    path('borrarPersona/', views.borrar_persona, name="borrarPersona"),
    path('doborrarPersona/', views.do_borrar_persona, name="doborrarPersona"),
    ##########################################################
    # VEHICLE URLS
    path('registrarVehiculo', views.nav_registrar_vehiculo, name="registroVehiculo"),
    path('doregistrarVehiculo', views.do_registrar_vehiculo, name="doregistroVehiculo"),
    path('listarVehiculo', views.listar_vehiculo, name="listarVehiculo"),
    path('editarVehiculo/', views.editar_vehiculo, name="editarVehiculo"),
    path('doeditarVehiculo/', views.do_actualizar_vehiculo, name="doeditarVehiculo"),
    path('borrarVehiculo/', views.borrar_vehiculo, name="borrarVehiculo"),
    path('doborrarVehiculo/', views.do_borrar_vehiculo, name="doborrarVehiculo"),

    ##########################################################
    # VISIT URLS
    path('registrarVisita', views.nav_registrar_visita, name="registroVisita"),
    path('doregistrarVisita', views.do_registrar_visita, name="doregistroVisita"),
    path('listarVisita', views.listar_visita, name="listarVisita"),
    path('editarVisita/', views.editar_visita, name="editarVisita"),
    path('doeditarVisita/', views.do_actualizar_visita, name="doeditarVisita"),
    path('borrarVisita/', views.borrar_visita, name="borrarVisita"),
    path('doborrarVisita/', views.do_borrar_visita, name="doborrarVisita"),

##########################################################
    # BLACKLIST URLS
    path('registrarBloqueo', views.nav_registrar_bloqueo, name="registroBloqueo"),
    path('doregistrarBloqueo', views.do_registrar_bloqueo, name="doregistroBloqueo"),
    path('listarBloqueo', views.listar_bloqueo, name="listarBloqueo"),
    path('editarBloqueo/', views.editar_bloqueo, name="editarBloqueo"),
    path('doeditarBloqueo/', views.do_actualizar_bloqueo, name="doeditarBloqueo"),
    path('borrarBloqueo/', views.borrar_bloqueo, name="borrarBloqueo"),
    path('doborrarBloqueo/', views.do_borrar_bloqueo, name="doborrarBloqueo"),
]
