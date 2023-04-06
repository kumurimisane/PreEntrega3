from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso

# Create your views here.

def curso(self, nombre, camada):
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()

    return HttpResponse(f"""
        <p> Curso: {curso.nombre} - Camada: {curso.camada} creado!</p>
    """)

def lista_cursos(self):
    lista = Curso.objects.all()
    return render(self, "App/lista.html", {"lista_cursos" : lista})

def inicio(self):
    return render(self, "inicio.html")
def cursos(self):
    return HttpResponse("vista de cursos")
def profesores(self):
    return HttpResponse("vista de profesores")
def estudiantes(self):
    return HttpResponse("vista de estudiantes")
def entregables(self):
    return HttpResponse("vista de entregables")