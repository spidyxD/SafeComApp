from django.db import models


# Create your models here.

class Person (models.Model):
    identification = models.CharField(max_length=12, primary_key=True)
    name = models.CharField(max_length=20)
    first_lastname = models.CharField(max_length=30)
    second_lastname = models.CharField(max_length=30)
    role = models.BooleanField()

    def __str__(self):
        return f"{self.identification} {self.name} {self.first_lastname}"


class Vehicle(models.Model):
    plate = models.CharField(max_length=7)
    model = models.CharField(max_length=20)
    brand = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='driver')

    def __str__(self):
        return self.plate


class RecordVisit(models.Model):
    """
    fecha_ingreso date,
    fecha_salida date,
    placa character varying(7) COLLATE pg_catalog."default",
    cedula_visita character varying(12) COLLATE pg_catalog."default",
    motivo character varying(500) COLLATE pg_catalog."default",
    """
    visit_id = models.AutoField(primary_key=True)
    incoming_date = models.DateTimeField(auto_now_add=True)
    outgoing_date = models.DateTimeField(null=True, blank=True) # format input_formats
    plate = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='vehicle')
    visit_identification = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='visitor') # one to many relationship
    reason = models.CharField(max_length=500)

    def __str__(self):
        incoming_date = self.incoming_date.strftime("%d-%m-%Y %H:%M:%S")
        outgoing_date = self.incoming_date.strftime("%d-%m-%Y %H:%M:%S")
        return f"{incoming_date} | {outgoing_date} | {self.plate} | {self.reason}"


class Blacklist(models.Model):
    """
    placa character varying(7) COLLATE pg_catalog."default",
    cedula character varying(12) COLLATE pg_catalog."default",
    """
    blacklist_id = models.AutoField(primary_key=True)
    visit_identification = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='visitor_black') # one to many relationship
    plate = models.CharField(max_length=7) #models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='vehicle_black')
    reason = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.visit_identification} {self.plate} {self.reason}"
