from django.contrib import admin
from .models import HealthCenter


@admin.register(HealthCenter)
class HealthCenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_centre', 'ville', 'est_ouvert')
    list_filter = ('type_centre', 'est_ouvert', 'ville')
    search_fields = ('name', 'ville')