from django.db import models

# Create your models here.


class Generation(models.Model):
    tension = models.IntegerField()
    corriente = models.IntegerField()
    velocidad_viento = models.IntegerField()
    direccion_viento = models.IntegerField()
