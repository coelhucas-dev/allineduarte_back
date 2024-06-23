from django.contrib import admin

from patients.models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'country_code', 'phone', 'email', 'birth_date']
    search_fields = ['name']
