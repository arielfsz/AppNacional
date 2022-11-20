from django.urls import path
from Datos.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("futbolistas/", futbolistas,name="futbolistas"),
    path("futbolistas/crear/", creacion_futbolistas,name="creacion_futbolistas"),
    path("futbolistas/buscar/", buscar_futbolista, name="buscar_futbolista"),
    path("futbolistas/buscar/resultados", resultados_buscar_futbolista, name="resultados_buscar_futbolista"),
    
    path("torneos/", torneos, name="torneos"),
    path("torneos/crear/", creacion_torneos,name="creacion_torneos"),

    path("tecnicos/", tecnicos, name="tecnicos"),
    path("tecnicos/crear/", creacion_tecnicos,name="creacion_tecnicos"),


]