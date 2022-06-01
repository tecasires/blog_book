from django.db import models

# Create your models here.

class Viajes(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    pais = models.CharField(max_length=40)
    precio = models.FloatField()
    EAN = models.CharField(max_length=13, unique=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'viaje'
        verbose_name_plural = 'viajes'


class Categorias(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
