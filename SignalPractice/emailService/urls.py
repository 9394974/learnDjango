from django.conf.urls import url

from emailService import views


urlpatterns = [
    url(r'^send/$', views.email_view),
]
