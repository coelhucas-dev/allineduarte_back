import logging
from django.db.models.signals import post_save
from django.dispatch import receiver

from allineduarte_back.settings import env
from appointments.models import Appointment
from utils.functions import send_email

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Appointment)
def send_mail(sender: Appointment, instance: Appointment, created, **kwargs):
    if created:
        ip = env('IP_HOST')

        appointment_date = instance.time.strftime('%d/%m/%Y às %H:%M')

        sender_mail = env('MAIL_HOST')
        sender_password = env('MAIL_PASSWORD')
        recipient_email = env.list('MAIL_RECIPIENT')
        subject = f'Pré Agendamento! {instance.patient.name} - {instance.patient.email}'
        body = (f'''
                    <html>
                      <body>
                        <h2>Você tem um novo pré agendamento marcado!</h2>
                        <p>Verifique a página de administrador para confirmar</p><br>
                        <p>Paciente: {instance.patient.name}</p>
                        <p>Email do paciente: {instance.patient.email}</p>
                        <p>Data do agendamento: {appointment_date}</p>
                        <br>
                        <a href="{ip}/admin/appointments/appointment/{instance.id}">Confirmar Agendamento</a></p>
                      </body>
                    </html>
                ''')
        send_email(sender_mail, sender_password, recipient_email, subject, body, logger)
