import re
from django.contrib import admin
from clinics.models import Clinic, ClinicHours, Plan


@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display = ['name', 'address1', 'country_code', 'phone']
    filter_horizontal = ('plans',)
    search_fields = ['name']


@admin.register(ClinicHours)
class ClinicHoursAdmin(admin.ModelAdmin):
    list_display = ['clinic', 'day_of_week', 'opening_time', 'closing_time']
    search_fields = ['clinic',]


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration']
    search_fields = ['name']
