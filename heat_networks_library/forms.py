from django import forms
from django.contrib.auth.models import User
from .models import Pipe


class PipeCreateForm(forms.ModelForm):
    class Meta:
        model = Pipe
        fields = [
            "name",
            "nominal_diameter",
            "outer_diameter",
            "wall_thickness",
            "weight_per_meter",
            "quality_standard",
        ]
        labels = {
            "name": "Наименование",
            "nominal_diameter": "Номинальный диаметр DN, Ду (может быть пустым)",
            "outer_diameter": "Наружный диаметр Ødн",
            "wall_thickness": "Список толщин стенок для данного диаметра s",
            "weight_per_meter": "Вес 1м трубы m",
            "quality_standard": "Наименование ГОСТа",
        }
