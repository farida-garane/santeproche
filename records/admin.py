from django.contrib import admin
from .models import MedicalRecord


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'soignant', 'health_center', 'date_consultation')
    list_filter = ('health_center', 'date_consultation')
    search_fields = ('patient__username', 'diagnostic')