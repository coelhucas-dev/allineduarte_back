import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.constants import COUNTRY_CODES


class Patient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    country_code = models.CharField(
        max_length=5, default='+55', choices=COUNTRY_CODES, verbose_name=_('Código do País'))
    phone = models.CharField(max_length=20, verbose_name=_('Telefone'))
    email = models.EmailField(verbose_name=_('Email'))
    birth_date = models.DateField(verbose_name=_('Data de nascimento'))

    class Meta:
        verbose_name = _('Paciente')
        verbose_name_plural = _('Pacientes')

    def __str__(self):
        return f'{self.name} || {self.email} || {self.country_code} {self.phone}'


class PatientProfile(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='patient_profile', verbose_name=_('Configurações do Paciente'))
    can_send_mail = models.BooleanField()
    can_send_whatsapp_message = models.BooleanField()
