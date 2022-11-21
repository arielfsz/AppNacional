from django.shortcuts import render
from Datos.models import *
from django.http import HttpResponse
from Datos.forms import *


def inicio(request):
    return render(request, 'Datos/padre.html')




def futbolistas(request):
    return render(request, 'Datos/futbolistas.html')

def creacion_futbolistas(request):
    if request.method == "POST":
        formulario = FutbolistaFormulario(request.POST)
               
        if formulario.is_valid():
            data=formulario.cleaned_data

            futbolista = Futbolista(nombre=data["nombre"], apellido=data["apellido"], nacimiento=data["nacimiento"],
            posicion=data["posicion"])

            futbolista.save()
 
    formulario = FutbolistaFormulario()    
    contexto = {"formulario": formulario}
    return render(request, 'Datos/futbolistas_formulario.html', contexto)




def tecnicos(request):
    return render(request, 'Datos/tecnicos.html')

def creacion_tecnicos(request):
    if request.method == "POST":
        formulario = TecnicoFormulario(request.POST)

        if formulario.is_valid():
            data=formulario.cleaned_data

            tecnico = Tecnico(nombre=data["nombre"], apellido=data["apellido"], nacimiento=data["nacimiento"])

            tecnico.save()
 
    formulario = TecnicoFormulario()    
    contexto = {"formulario": formulario}
    return render(request, 'Datos/tecnicos_formulario.html', contexto)




def torneos(request):
    return render(request, 'Datos/torneos.html')

def creacion_torneos(request):
    if request.method == "POST":
        formulario = TorneoFormulario(request.POST)

        if formulario.is_valid():
            data=formulario.cleaned_data

            torneo = Torneo(nombre=data["nombre"], año=data["año"], caracter=data["caracter"],
            nacionalidad=data["nacionalidad"])

            torneo.save()
 
    formulario = TorneoFormulario()    
    contexto = {"formulario": formulario}
    return render(request, 'Datos/torneos_formulario.html', contexto)



def buscar_futbolista(request):
    return render(request, "Datos/buscar_futbolista.html")


def resultados_buscar_futbolista(request):
    nombre_futbolista = request.GET["nombre_jugador"]
    futbolistas = Futbolista.objects.filter(apellido__contains=nombre_futbolista)
    return render(request, "Datos/resultados_buscar_futbolista.html", {"futbolistas":futbolistas})
