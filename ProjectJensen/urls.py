# from django.contrib import admin
# from django.urls import path
# from ProjectJensen.views import home, proyectos, tareas, equipos, miembros_equipo
#
## urlpatterns = [
##    path('admin/', admin.site.urls),
## ]
#
# urlpatterns = [
#    path("admin/", admin.site.urls),
#    path("", home, name="home"),
#    path("proyectos/", proyectos, name="proyectos"),
#    path("tareas/", tareas, name="tareas"),
#    path("equipos/", equipos, name="equipos"),
#    path("miembros_equipo/", miembros_equipo, name="miembros_equipo"),
# ]

from django.contrib import admin
from django.urls import path
import ProjectJensen.views as views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("proyectos/", views.proyectos, name="proyectos"),
    path("tareas/", views.tareas, name="tareas"),
    path("equipos/", views.equipos, name="equipos"),
    path("miembros_equipo/", views.miembros_equipo, name="miembros_equipo"),
]
