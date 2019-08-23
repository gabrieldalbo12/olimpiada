from django.db import models

# Create your models here.


class Generation(models.Model):
    tension = models.IntegerField()
    corriente = models.IntegerField()
    velocidad_viento = models.IntegerField()
    DIRECCION_VIENTO = [
        ('ESTE', 'Este'),
        ('OESTE', 'Oeste'),
        ('NORTE', 'Norte'),
        ('SUR', 'Sur'),
    ]
    direccion_viento = models.CharField(
        max_length=10,
        choices=DIRECCION_VIENTO,
        default='ESTE',
    )


    def __str__(self):
        return '{}, {}, {}, {}'.format(self.tension, self.corriente, self.velocidad_viento, self.direccion_viento)
