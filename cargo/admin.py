from django.contrib import admin

# Register your models here.

from .models import Airport,Country,Special_uld,Suspicious_good,Awb_distribution,Awb_info

admin.site.register(Airport)
admin.site.register(Country)
admin.site.register(Special_uld)
admin.site.register(Suspicious_good)
admin.site.register(Awb_distribution)
admin.site.register(Awb_info)