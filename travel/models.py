from django.db import models

class Travels(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=40)
    price = models.FloatField()
    EAN = models.CharField(max_length=13, unique=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'viaje'
        verbose_name_plural = 'viajes'
        
    def __str__(self):
        return self.name + " | " + self.country + " | " + self.EAN + " | " + str(self.price)


class Categories(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
    
    def __str__(self):
        return self.name + " | " + self.description
