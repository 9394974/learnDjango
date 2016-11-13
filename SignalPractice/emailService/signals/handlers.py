from django.core.mail import EmailMessage


def email_service(sender, **kwargs):
    email = EmailMessage(
        subject=kwargs.get('subject'),
        body=kwargs.get('content'),
        from_email=kwargs.get('email_sender'),
        to=kwargs.get('email_receiver')
    )
    email.send()
