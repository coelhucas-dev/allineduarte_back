from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer


class AppointmentCreateView(CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
