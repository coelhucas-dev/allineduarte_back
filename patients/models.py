from django.db import models
from django.forms import CharField
from django.utils.translation import gettext_lazy as _

from utils.constants import COUNTRY_CODES


class Patient(models.Model):
    name = CharField(max_length=255)
    country_code = models.CharField(
        max_length=5, default='+55', choices=COUNTRY_CODES, verbose_name=_('Código do País'))
    phone = models.CharField(max_length=20, verbose_name=_('Telefone'))
    email = models.EmailField()
    birth_date = models.DateField(verbose_name=_('Data de nascimento'))


class PatientProfile(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='patient_profile', verbose_name=_('Configurações do Paciente'))
    can_send_mail = models.BooleanField()
    can_send_whatsapp_message = models.BooleanField()
