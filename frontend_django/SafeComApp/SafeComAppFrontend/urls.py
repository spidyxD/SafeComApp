from django.urls import path
from . import views


urlpatterns = [
    #####################################
    # INDEX/HOME
    path('', views.home, name='index'),
    path('registrarPersona', views.registrar_persona, name="registroPersona")
]
