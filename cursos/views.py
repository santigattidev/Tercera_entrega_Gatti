from django.shortcuts import render
from .forms import CrearCurso
from .models import Curso

# Create your views here.
def cursos(request):
  mensaje= ''
  formulario = CrearCurso(request.POST)
  if formulario.is_valid():
    data = formulario.cleaned_data
    curso = Curso(nombre=data.get('nombre'), camada=data.get('camada'))
    curso.save()
    mensaje = 'Guardado correctamente'
  formulario = CrearCurso()
  
  return render(request, 'cursos.html', {'formulario': formulario,'se_guardo': mensaje})