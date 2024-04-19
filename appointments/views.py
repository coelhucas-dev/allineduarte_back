from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer, ScheduledSerializer


class AppointmentCreateView(CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class ScheduledView(APIView):
    @staticmethod
    def get(req):
        serializer = ScheduledSerializer(data=req.data)
        if serializer.is_valid():
            scheduled_times = serializer.data
            return Response(scheduled_times, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
