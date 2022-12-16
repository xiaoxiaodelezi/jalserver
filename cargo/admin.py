from django.contrib import admin

# Register your models here.

from .models import Airport,Country,Special_uld

admin.site.register(Airport)
admin.site.register(Country)
admin.site.register(Special_uld)