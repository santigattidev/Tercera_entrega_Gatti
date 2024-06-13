from django.shortcuts import render
from .forms import EstudianteForm
from .models import Estudiante

# Create your views here.
def estudiantes(request):
  if request.method == 'POST':
    formulario = EstudianteForm(request.POST)
    if formulario.is_valid():
      data = formulario.cleaned_data
      estudiante = Estudiante(nombre=data.get('nombre'), apellido=data.get('apellido'), email=data.get('email'))
      estudiante.save()
  formulario = EstudianteForm()
  
  return render(request, 'estudiantes.html', {'formulario': formulario})