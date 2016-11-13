from django.shortcuts import HttpResponse
from django.dispatch import Signal, receiver

import time

# Create your views here.

hello_signal = Signal(providing_args=[])


@receiver(hello_signal)
def print_hello(sender, **kwargs):
    time.sleep(5)
    print("hello world")


def hello(request):
    hello_signal.send(__name__)
    return HttpResponse("OK")

