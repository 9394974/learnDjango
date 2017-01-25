from django.db import models

# Create your models here.

NAME_LENGTH_LIMIT = 50

INTRO_LENGTH_LIMIT = 200


class Courses(models.Model):

    name = models.CharField(max_length=NAME_LENGTH_LIMIT)
    intro = models.CharField(max_length=INTRO_LENGTH_LIMIT)
