from django.conf import settings
from django.db import models
class Hello(models.Model):
    'Generated Model'
    name = models.CharField(max_length=256,)
class Hi(models.Model):
    'Generated Model'
    name = models.CharField(max_length=256,)
