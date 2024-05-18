from django.db import models

# Create your models here.
class Pipe(models.Model):
    name = models.CharField(max_length=255) 
    nominal_diameter = models.IntegerField() # Номинальный диаметр
    outer_diameter = models.DecimalField(max_digits=10, decimal_places=2) # Наружный диаметр
    wall_thickness = models.DecimalField(max_digits=5, decimal_places=2)
    weight_per_meter = models.DecimalField(max_digits=10, decimal_places=2)
    quality_standard = models.CharField(max_length=100)

