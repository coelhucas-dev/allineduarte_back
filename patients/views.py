from rest_framework.generics import ListCreateAPIView

from patients.models import Patient
from patients.serializers import ListCreatePatientSerializer


class ListCreatePatientView(ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = ListCreatePatientSerializer
