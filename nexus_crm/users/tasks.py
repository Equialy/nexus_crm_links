from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
import logging

from django.template.loader import render_to_string

logger = logging.getLogger(__name__)

@shared_task
def send_welcome_email(email, first_name):
    subject = render_to_string('emails/welcome_subject.txt', {"first_name": first_name}).strip()
    message = render_to_string('emails/welcome_message.txt', {'first_name': first_name})
    html_message = render_to_string('emails/welcome_message.html', {'first_name': first_name})
    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
            html_message=html_message
        )
        logger.info(f"Welcome email sent to {email}")
    except Exception as e:
        logger.error(f"Failed to send welcome email to {email}: {str(e)}")
        raise

@shared_task
def send_password_reset_email(email, user_id):
    from .models import UserProfile
    from django.urls import reverse
    from django.contrib.auth.tokens import default_token_generator
    from django.utils.http import urlsafe_base64_encode
    from django.utils.encoding import force_bytes

    logger.info(f"Starting password reset email task for {email}, user_id={user_id}")
    try:
        user = UserProfile.objects.get(pk=user_id)
        token = default_token_generator.make_token(user)
        # uid = urlsafe_base64_encode(force_bytes(user.pk))
        reset_url = f"{settings.SITE_URL}{reverse('users:password_reset_confirm', kwargs={'user_id': user.pk, 'token': token})}"
        subject = render_to_string(
            'emails/password_reset_subject.txt',
            {'user': user, 'reset_url': reset_url}
        ).strip()

        message = render_to_string(
            'emails/password_reset_message.txt',
            {'user': user, 'reset_url': reset_url}
        )

        html_message = render_to_string(
            'emails/link_to_reset_password_message.html',
            {'user': user, 'reset_url': reset_url}
        )
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
            html_message=html_message
        )
        logger.info(f"Password reset email sent to {email}")
    except Exception as e:
        logger.error(f"Failed to send password reset email to {email}: {str(e)}")
        raise