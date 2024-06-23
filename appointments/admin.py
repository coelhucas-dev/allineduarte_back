from django.contrib import admin

from appointments.models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'clinic', 'plan', 'time', 'confirmed']
    search_fields = ['patient__name']
    list_filter = ['clinic', 'confirmed']
    list_editable = ['confirmed']
