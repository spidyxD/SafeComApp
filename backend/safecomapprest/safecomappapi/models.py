from django.db import models


# Create your models here.

class Vehicle(models.Model):
    plate = models.CharField(max_length=7)
    model = models.CharField(max_length=20)
    brand = models.CharField(max_length=10)
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.plate


class Person (models.Model):
    identification = models.CharField(max_length=12)
    name = models.CharField(max_length=20)
    first_lastname = models.CharField(max_length=30)
    second_lastname = models.CharField(max_length=30)
    role = models.BooleanField()

    def __str__(self):
        return self.name


class recordVisit(models.Model):
    """
    fecha_ingreso date,
    fecha_salida date,
    placa character varying(7) COLLATE pg_catalog."default",
    cedula_visita character varying(12) COLLATE pg_catalog."default",
    motivo character varying(500) COLLATE pg_catalog."default",
    """
    incoming_date = models.DateTimeField(auto_now_add=True)
    outgoing = models.DateTimeField(null=True, blank=True)
    plate = models.CharField(max_length=7)

    pass
