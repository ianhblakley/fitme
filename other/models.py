from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class FitMeUser(models.Model):
    user = models.OneToOneField(User)
    age = models.IntegerField()
    height = models.IntegerField()


class WeightLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    weight = models.FloatField()


class BodyFatLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    body_fat = models.FloatField()