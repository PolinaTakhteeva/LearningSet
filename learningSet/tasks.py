from __future__ import absolute_import, unicode_literals
from django.core.mail import send_mail
from celery import shared_task

@shared_task
def add(x, y):
    return x + y


@shared_task
def send_email():
	return send_mail(
    	'Subject here',
    	'Here is the message.',
    	'polinatahteeva@gmail.com',
    	['polinatahteeva@gmail.com'],
    	fail_silently=False,
	)