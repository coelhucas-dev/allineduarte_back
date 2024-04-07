from django.contrib import admin

from appointments.models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['clinic', 'time', 'confirmed']
    search_fields = ['clinic__name']
    list_editable = ['confirmed']
