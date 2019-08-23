from django.db import models

# Create your models here.


class Eolica(models.Model):
    i = models.FloatField()
    w_s = models.FloatField()
    w_d = models.CharField(max_length=20)
    r = [
        ('ESTE', 'Este'),
        ('OESTE', 'Oeste'),
        ('NORTE', 'Norte'),
        ('SUR', 'Sur'),
        ('NOR ESTE', 'Nor este'),
        ('NOR OESTE', 'Nor oeste'),
        ('SUR OESTE', 'Sur oeste'),
        ('SUR ESTE', 'Sur este'),
    ]
    r = models.CharField(
        max_length=10,
        choices=r,
        default='ESTE',
    )


    def __str__(self):
        return '{}, {}, {}, {}'.format(self.i, self.w_s, self.w_d, self.r)
