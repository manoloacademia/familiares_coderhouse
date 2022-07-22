from django.db import models


# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    parentezco = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateTimeField()

    def __str__(self):
        return self.name
