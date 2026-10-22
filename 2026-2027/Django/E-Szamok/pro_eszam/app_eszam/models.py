from socketserver import ForkingTCPServer
from django.db import models

# Create your models here.

class Adalek(models.Model):
    
    kod = models.CharField(max_length=32, primary_key=True)
    nev = models.CharField(max_length=128)
    mellekhatas = models.BooleanField(default=0)

    class Meta:
        verbose_name = "adalék"
        verbose_name_plural = "adalékok"

    def __str__(self):
        return self.nev

class Funkcio(models.Model):
    
    az = models.AutoField(primary_key=True)
    kod = models.CharField(max_length=128)
    fnev = models.CharField(max_length=128)

    class Meta:
        verbose_name = "funkció"
        verbose_name_plural = "funkciók"

    def __str__(self):
        return self.kod

