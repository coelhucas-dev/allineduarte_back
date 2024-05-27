import datetime
from django.utils import timezone
from rest_framework import serializers

from appointments.models import Appointment
from clinics.models import ClinicHours, Plan


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['clinic', 'plan', 'time']
        
    def validate_time(self, value: datetime.datetime):
        if not self.initial_data:
            raise serializers.ValidationError('Please send a valid payload')
        clinic_id = self.initial_data.get('clinic')
        
        if clinic_id is None:
            raise serializers.ValidationError('Please send a valid Clinic ID on payload')
        
        clinic_hours = ClinicHours.objects.filter(clinic=clinic_id)
        is_in_clinic_hours = False
        for hour in clinic_hours:    
            if value.isoweekday == hour.day_of_week:
                is_in_clinic_hours = True
        
        if not is_in_clinic_hours:
            raise serializers.ValidationError('Date not available for this clinic')
        existing_appointment = Appointment.objects.filter(time=value, confirmed=True).exists()
        if existing_appointment:
            raise serializers.ValidationError(
                f"Já existe um agendamento para este horário: {value}")
        return value
    


class ScheduledSerializer(serializers.Serializer):

    @staticmethod
    def to_representation(instance, **kwargs):
        scheduled_times = []
        appointments = Appointment.objects.filter(
            time__gte=timezone.now())

        plans = Plan.objects.all()
        if not appointments:
            return {'scheduled': scheduled_times}

        for appointment in appointments.values():
            appointment['time'] = timezone.localtime(appointment['time'])
            time = appointment['time']
            plan_id = appointment['plan_id']
            plan = plans.filter(id=plan_id).values().first()
            if not plan: continue
            scheduled_times.append({
                'appointment': appointment,
                'plan': {
                    'id': plan['id'],
                    'name': plan['name'],
                    'duration': plan['duration'].total_seconds() / 3600
                },
                'scheduled_time': {
                    'day': time.date(),
                    'hour': time.time()
                }
            })

        return {'scheduled': scheduled_times}
