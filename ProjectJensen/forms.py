from django import forms
from .models import Proyecto, Tarea, Equipo, MiembroEquipo


# Clase para que tome el Datepicker
class DateInput(forms.DateInput):
    input_type = "text"
    attrs = {"class": "datepicker form-control"}


# 🎨 Formulario para el modelo Proyecto
class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = "__all__"  # 📋 Incluye todos los campos del modelo en el formulario
        widgets = {
            "fecha_inicio": DateInput(),
            "fecha_fin": DateInput(),
        }


# 📝 Formulario para el modelo Tarea
class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = "__all__"
        widgets = {
            "fecha_inicio": DateInput(),
            "fecha_fin": DateInput(),
        }


# 🏢 Formulario para el modelo Equipo
class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = "__all__"


# 👥 Formulario para el modelo MiembroEquipo
class MiembroEquipoForm(forms.ModelForm):
    class Meta:
        model = MiembroEquipo
        fields = "__all__"


# 🔍 Formulario de búsqueda
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
        label="Buscar en",  # 🗂️ Campo de selección para especificar dónde buscar
    )
