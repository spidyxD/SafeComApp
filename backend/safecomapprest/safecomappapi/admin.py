from django.contrib import admin

# Register your models here.

from .models import (
    Vehicle,
    Person
)

admin.site.register(Vehicle)
admin.site.register(Person)