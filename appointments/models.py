from django.db import models
from django.utils.translation import gettext_lazy as _

from clinics.models import Clinic, Plan


class Appointment(models.Model):
    clinic = models.ForeignKey(
        Clinic, on_delete=models.PROTECT, related_name='clinic', verbose_name=_('Clínica'))
    plan = models.ForeignKey(
        Plan, on_delete=models.PROTECT, related_name='plan', verbose_name=_('Plano'))
    time = models.DateTimeField(verbose_name=_('Dia e Horário'), unique=True)
    confirmed = models.BooleanField(verbose_name=_('Confirmado'))

    class Meta:
        verbose_name = _('Agendamento')
        verbose_name_plural = _('Agendamentos')
