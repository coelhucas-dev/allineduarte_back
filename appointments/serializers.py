from django.utils import timezone
from rest_framework import serializers

from appointments.models import Appointment
from clinics.models import Plan


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

    @staticmethod
    def validate_time(value):
        existing_appointment = Appointment.objects.filter(time=value).exists()
        if existing_appointment:
            raise serializers.ValidationError(
                "Já existe um agendamento para este horário.")
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
