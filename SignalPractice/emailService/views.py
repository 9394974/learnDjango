from django.shortcuts import render, HttpResponse
from django.conf import settings

from emailService.signals import email_signal

# Create your views here.


def email_view(request):
    info = {
        'email_sender': settings.EMAIL_HOST_USER,
        'email_receiver': settings.EMAIL_RECIPIENT,
        'subject': "Hello, I'm signal",
        'content': 'signal email test'
    }
    email_signal.send(sender=__name__, **info)
    return HttpResponse("OK")
