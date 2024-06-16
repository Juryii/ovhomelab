from decimal import Decimal
from django import forms
from .models import Pipe


class PipeCreateForm(forms.ModelForm):
    weight_per_meter = forms.DecimalField(required=False, label="Вес 1м трубы m")
    class Meta:
        model = Pipe
        fields = [
            "nominal_diameter",
            "outer_diameter",
            "wall_thickness",
            "weight_per_meter",
            "quality_standard",
        ]
        labels = {
            "nominal_diameter": "Номинальный диаметр DN, Ду (может быть пустым)",
            "outer_diameter": "Наружный диаметр Ødн",
            "wall_thickness": "Список толщин стенок для данного диаметра s",
            "weight_per_meter": "Вес 1м трубы m",
            "quality_standard": "Наименование ГОСТа",
        }
    def clean_weight_per_meter(self):
        weight_per_meter = self.cleaned_data.get("weight_per_meter")
        if weight_per_meter is None:
            outer_diameter = self.cleaned_data.get("outer_diameter")
            wall_thickness = self.cleaned_data.get("wall_thickness")
            if outer_diameter and wall_thickness:
                return self.calculate_pipe_weights(outer_diameter, wall_thickness)
        return weight_per_meter
    
    def save(self, commit=True):
        instance = super(PipeCreateForm, self).save(commit=False)
        instance.weight_per_meter = self.cleaned_data["weight_per_meter"]
        instance.name = f"Труба Ø{self.cleaned_data['outer_diameter']} {self.cleaned_data['quality_standard']}"
        if commit:
            instance.save()
        return instance

    def calculate_pipe_weights(self, outer_diameter, wall_thickness):
        calculated_weight = []
        for thickness in wall_thickness:
            weight = Decimal(0.02466) * thickness * (outer_diameter - thickness)
            calculated_weight.append(weight)
        return calculated_weight
