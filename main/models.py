from django.db import models

# Create your models here.
from django.db import models

class SouthIndian(models.Model):
    name = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return {self.name}

class American(models.Model):
    name = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=8, decimal_places=2)
    

    def __str__(self):
        return {self.name}