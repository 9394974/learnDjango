from django.apps import AppConfig

from emailService.signals import email_signal
from emailService.signals.handlers import email_service

import hashlib


class EmailserviceConfig(AppConfig):
    name = 'emailService'

    def ready(self):
        func_uid = hashlib.sha256('email_service'.encode()).hexdigest()
        email_signal.connect(email_service, dispatch_uid=func_uid)
