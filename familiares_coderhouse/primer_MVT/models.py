from django.db import models


# Create your models here.
class Familiar(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    age = models.IntegerField()
    birthday = models.DateTimeField()

    def __str__(self):
        return self.name
