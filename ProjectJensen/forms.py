from django import forms
from .models import Proyecto, Tarea, Equipo, MiembroEquipo


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = "__all__"


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = "__all__"


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = "__all__"


class MiembroEquipoForm(forms.ModelForm):
    class Meta:
        model = MiembroEquipo
        fields = "__all__"


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label="Buscar")
    search_in = forms.ChoiceField(
        choices=[
            ("proyectos", "Proyectos"),
            ("tareas", "Tareas"),
            ("equipos", "Equipos"),
            ("miembros", "Miembros del Equipo"),
        ],
        required=False,
        label="Buscar en",
    )
