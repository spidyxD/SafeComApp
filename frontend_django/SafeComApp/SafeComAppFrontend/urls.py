from django.urls import path
from . import views


urlpatterns = [
    ##########################################################
    # PERSONA URLS
    path('', views.home, name='index'),
    path('registrarPersona', views.registrar_persona, name="registroPersona"),
    path('listarPersona', views.listar_persona, name="listarPersona"),
    ##########################################################
    # VEHICLE URLS
    ##########################################################
    # VISIT URLS
]
