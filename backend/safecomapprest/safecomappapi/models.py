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
    identification = models.CharField(max_length=12, primary_key=True)
    name = models.CharField(max_length=20)
    first_lastname = models.CharField(max_length=30)
    second_lastname = models.CharField(max_length=30)
    role = models.BooleanField()

    def __str__(self):
        return f"{self.identification} {self.name} {self.first_lastname}"


class RecordVisit(models.Model):
    """
    fecha_ingreso date,
    fecha_salida date,
    placa character varying(7) COLLATE pg_catalog."default",
    cedula_visita character varying(12) COLLATE pg_catalog."default",
    motivo character varying(500) COLLATE pg_catalog."default",
    """
    incoming_date = models.DateTimeField(auto_now_add=True)
    outgoing_date = models.DateTimeField(null=True, blank=True)
    plate = models.CharField(max_length=7)
    visit_identification = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='visitor') # one to many relationship
    reason = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.incoming_date} {self.outgoing_date} {self.plate} {self.reason}"


class Blacklist(models.Model):
    """
    placa character varying(7) COLLATE pg_catalog."default",
    cedula character varying(12) COLLATE pg_catalog."default",
    """
    visit_identification = models.CharField(max_length=12)
    plate = models.CharField(max_length=7)
    reason = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.visit_identification} {self.plate} {self.reason}"
