from django.urls import path

from clinics.views import ClinicView

urlpatterns = [
    path('', ClinicView.as_view(), name='clinic'),
]
