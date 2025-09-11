from django.contrib import admin
from carsapp.models import Company,Products

# Register your models here.

admin.site.register([Company,Products])
