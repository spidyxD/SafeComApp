from django.urls import path
from . import views


urlpatterns = [
    ##########################################################
    # PERSONA URLS
    path('', views.home, name='index'),
    path('registrarPersona', views.nav_registrar_persona, name="registroPersona"),
    path('doregistrarPersona', views.do_registrar_persona, name="doregistroPersona"),
    path('listarPersona', views.listar_persona, name="listarPersona"),
    path('editarPersona', views.editar_persona, name="editarPersona"),
    ##########################################################
    # VEHICLE URLS
    ##########################################################
    # VISIT URLS
]
