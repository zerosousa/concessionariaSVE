from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Moto(models.Model):
    ano = models.CharField(max_length=200)
    cor = models.CharField(max_length=200)
