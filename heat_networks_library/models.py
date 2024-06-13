""" импорт еобходимых модулей """

from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Pipe(models.Model):
    """Клас трубы без изоляции"""

    name = models.CharField(max_length=255)  # улосвное обозначение
    nominal_diameter = models.IntegerField(
        blank=True, null=True
    )  # Номинальный диаметр DN, Ду
    outer_diameter = models.DecimalField(
        max_digits=10, decimal_places=2
    )  # Наружный диаметр dн
    wall_thickness = ArrayField(
        models.DecimalField(max_digits=4, decimal_places=2)
    )  # Список толщин стенок для данного диаметра s
    weight_per_meter = ArrayField(
        models.DecimalField(max_digits=6, decimal_places=2)
    )  # вес 1м трубы m
    quality_standard = models.CharField(
        max_length=100
    )  # Наименование ГОСТа трубы ГОСТ 8732-78

    def __str__(self) -> str:
        return str(self.name)
