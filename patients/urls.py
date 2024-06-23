from django.urls import path
from patients.views import ListCreatePatientView

urlpatterns = [
    path('', ListCreatePatientView.as_view(), name='list_create_patient'),
]
