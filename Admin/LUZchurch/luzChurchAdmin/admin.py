from django.contrib import admin
from .models import *
# Register your models here.


class ShowOfficeHistoryDetails(admin.ModelAdmin):
    list_display = ("short_history", "church_office", "church_mobile")

class ShowMotoDetails(admin.ModelAdmin):
    list_display = ("moto",)

admin.site.register(OfficeHistory,ShowOfficeHistoryDetails)
admin.site.register(Moto,ShowMotoDetails)