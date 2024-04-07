from rest_framework import serializers

from clinics.models import Clinic, ClinicHours, Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class ClinicHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicHours
        fields = ['day_of_week', 'opening_time', 'closing_time']


class ClinicSerializer(serializers.ModelSerializer):
    plans = PlanSerializer(many=True, read_only=True)
    clinic_hours = ClinicHoursSerializer(
        many=True, read_only=True, source='clinic_hours.all')

    class Meta:
        model = Clinic
        fields = '__all__'
