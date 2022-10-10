from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import formularioComentarios
from datetime import datetime

# Create your views here.

def index(request):

    titulo = "Aplicacion"

    if request.method == "GET":
        return render(request, "index.html", {
            "title": titulo
        })

    elif request.method == "POST":

        print("\n el archivo es el siguiente: ", request.POST['excel'], "\n")
        return redirect("/")


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
        return redirect("/comentarios/")
    
    


    

def contacto(request):

    return render(request, "contacto.html")

