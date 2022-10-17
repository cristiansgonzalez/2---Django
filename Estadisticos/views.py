from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import formularioComentarios, ArchivoExcel
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from .Analisis import *
import pandas as pd
import numpy as np
import statistics
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext

# Create your views here.

@csrf_protect
def index(request):

    titulo = "Aplicacion"

    if request.method == "GET":
        return render(request, "index.html", {
            "title": titulo,
            #"formExcel": ArchivoExcel(),
        })

    elif request.method == "POST":
        
        contenido ={}
        archivo = request.FILES["excel"]
        tipo = request.POST["tipo"]
        Numero_actividades = int(request.POST["Numero_actividades"])
        Puntaje_actividad = int(request.POST["Puntaje_actividad"])
        actividad = int(request.POST["actividad"])
        print(archivo.name)
        
        fs = FileSystemStorage()
        direccion =fs.save(fs.get_valid_name(archivo.name), archivo)
        
        reporte = Analisis_Curso(archivo.name, Puntaje_actividad, actividad, Numero_actividades, 'no', tipo)
        print(reporte)
        fs.delete(archivo.name)  
        
        contenido['url'] = fs.url(direccion)
        print("Esta es la direccion: ", contenido.values)
        
        return render("descarga.html", {
            "title": "Descargar",
            "url": reporte,
        })  
        '''
        #return redirect("/")
        
        return render(request, "descarga.html", {
            "title": "Descargar",
            #"url": fs.url(direccion),
            #"url": fs.url(reporte),
            "url": reporte,
        })
        '''

@csrf_protect
def comentarios(request):

    titulo = "Comentarios"
    datos_servidor = Usuario.objects.all()

    if request.method == "GET":
        return render(request, "comentarios.html", {
            "title": titulo,
            "datos": datos_servidor,
            "form": formularioComentarios(),
        })

    elif request.method == "POST":

        now = datetime.now()
        Usuario.objects.create(nombre = request.POST['nombreForm'], comentario = request.POST['comentarioForm'], fecha = now)
        #return redirect("/comentarios/")
        
        return render(request, "comentarios.html", {
            "title": titulo,
            "datos": datos_servidor,
            "form": formularioComentarios(),
        })
        '''
        '''

def contacto(request):

    return render(request, "contacto.html")

