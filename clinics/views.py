from rest_framework import generics

from clinics.serializers import ClinicSerializer
from clinics.models import Clinic


class ClinicView(generics.ListAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
