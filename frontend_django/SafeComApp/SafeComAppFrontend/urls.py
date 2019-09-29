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
    ##########################################################
    # VISIT URLS
]
