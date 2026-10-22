from socketserver import ForkingTCPServer
from django.db import models

# Create your models here.

class Adalek(models.Model):
    
    kod = models.IntegerField(default=0, primary_key=True)
    nev = models.CharField(max_length=128)
    mellekhatas = models.BooleanField(default=0)

    class Meta:
        verbose_name = "Adalék"
        verbose_name_plural = "Adalékok"

    def __str__(self):
        return self.name

class Funkcio(models.Model):
    
    az = models.IntegerField()
    kod = models.CharField(max_length=128)
    fnev = models.CharField(max_length=128)

    class Meta:
        verbose_name = "funkció"
        verbose_name_plural = "funkciók"

    def __str__(self):
        return self.name

