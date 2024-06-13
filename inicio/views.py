from django.shortcuts import render
from .forms import BuscarCurso
from cursos.models import Curso

# Create your views here.

def index(request):
  formulario = BuscarCurso(request.GET)
  if formulario.is_valid():
    nombre = formulario.cleaned_data.get('nombre')
    cursos = Curso.objects.filter(nombre__icontains=nombre)

  
  return render(request, 'inicio/index-modified.html', {'cursos':cursos, 'buscador': formulario})

