from django.contrib import admin

# Register your models here.

from .models import (
    Vehicle,
    Person,
    RecordVisit,
    Blacklist,
)

admin.site.register(Vehicle)
admin.site.register(Person)
admin.site.register(RecordVisit)
admin.site.register(Blacklist)
