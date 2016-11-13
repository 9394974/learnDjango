from django.conf.urls import url

from helloService import views


urlpatterns = [
    url(r'', views.hello)
]