import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from appointments.models import Appointment
from utils.send_mail import send_email

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Appointment)
def send_mail(sender, instance, **kwargs):
    sender_mail = 'lucas.dcs.dev@gmail.com'
    sender_password = '12092003ldc'
    recipient_email = 'lucas.dcs.dev@gmail.com'
    subject = 'test'
    body = 'test'

    # send_email(sender_mail, sender_password, recipient_email, subject, body)
