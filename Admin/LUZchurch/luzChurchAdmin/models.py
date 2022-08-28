from django.db import models

# Create your models here.

class Moto(models.Model):
    moto = models.TextField()

class OfficeHistory(models.Model):
    short_history = models.TextField()
    church_office = models.IntegerField()
    church_mobile = models.IntegerField()
