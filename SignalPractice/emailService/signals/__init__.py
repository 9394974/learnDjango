from django.dispatch import Signal


email_signal = Signal(providing_args=['email_sender', 'email_receiver', 'subject', 'content'])
