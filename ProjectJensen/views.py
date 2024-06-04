from django.shortcuts import render
from .models import Proyecto, Tarea, Equipo, MiembroEquipo
from .forms import ProyectoForm, TareaForm, EquipoForm, MiembroEquipoForm, SearchForm


def home(request):
    form = SearchForm()
    results = []
    show_latest_projects = False
    latest_projects_data = []

    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data.get("query")
            search_in = form.cleaned_data.get("search_in")

            if "search" in request.POST:
                if search_in == "proyectos":
                    results = Proyecto.objects.filter(
                        nombre__icontains=query
                    ) | Proyecto.objects.filter(descripcion__icontains=query)
                elif search_in == "tareas":
                    results = Tarea.objects.filter(
                        nombre__icontains=query
                    ) | Tarea.objects.filter(descripcion__icontains=query)
                elif search_in == "equipos":
                    results = Equipo.objects.filter(
                        nombre__icontains=query
                    ) | Equipo.objects.filter(descripcion__icontains=query)
                elif search_in == "miembros":
                    results = (
                        MiembroEquipo.objects.filter(nombre__icontains=query)
                        | MiembroEquipo.objects.filter(apellido__icontains=query)
                        | MiembroEquipo.objects.filter(rol__icontains=query)
                    )
            elif "latest_projects" in request.POST:
                show_latest_projects = True
                latest_projects = Proyecto.objects.all().order_by("-id")[:5]
                for proyecto in latest_projects:
                    tareas = Tarea.objects.filter(proyecto=proyecto)
                    equipos = Equipo.objects.filter(
                        id__in=tareas.values_list("equipo", flat=True)
                    ).distinct()
                    miembros = MiembroEquipo.objects.filter(
                        equipo__in=equipos
                    ).distinct()
                    latest_projects_data.append(
                        {
                            "proyecto": proyecto,
                            "tareas": tareas,
                            "equipos": equipos,
                            "miembros": miembros,
                        }
                    )

    context = {
        "form": form,
        "results": results,
        "show_latest_projects": show_latest_projects,
        "latest_projects_data": latest_projects_data,
    }
    return render(request, "home.html", context)


def proyectos(request):
    if request.method == "POST":
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProyectoForm()
    proyectos = Proyecto.objects.all()
    return render(request, "proyectos.html", {"form": form, "proyectos": proyectos})


def tareas(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TareaForm()
    tareas = Tarea.objects.all()
    return render(request, "tareas.html", {"form": form, "tareas": tareas})


def equipos(request):
    if request.method == "POST":
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EquipoForm()
    equipos = Equipo.objects.all()
    return render(request, "equipos.html", {"form": form, "equipos": equipos})


def miembros_equipo(request):
    if request.method == "POST":
        form = MiembroEquipoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MiembroEquipoForm()
    miembros = MiembroEquipo.objects.all()
    return render(request, "miembros_equipo.html", {"form": form, "miembros": miembros})
