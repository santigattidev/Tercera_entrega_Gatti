from django.shortcuts import render,redirect
from .models import Profesor

# # Create your views here.

# v1
#
# def profesores(request):
#   print('valor del GET',request.GET)
#   print('valor del POST',request.POST)
#   if request.method == 'POST':
#     profesor = Profesor(nombre=request.POST.get('nombre'), apellido=request.POST.get('apellido'), email=request.POST.get('email'), profesión=request.POST.get('profesion'))
#     profesor.save()
#   return render(request, 'profesores/profesores.html')


# v2
from .forms import ProfesorForm

def profesores(request):
  print('valor del GET',request.GET)
  print('valor del POST',request.POST)
  if request.method == 'POST':
    pass
    formulario = ProfesorForm(request.POST)
    if formulario.is_valid():
      datos = formulario.cleaned_data
      profesor = Profesor(nombre=datos.get('nombre'), apellido=datos.get('apellido'), email=datos.get('email'), profesión=datos.get('profesion'))
      profesor.save()
      return redirect('/')
  formulario = ProfesorForm()
  return render(request, 'profesores/profesores.html', {'formulario': formulario})

def profesoresLista(request):
  profesores = Profesor.objects.all()
  return render(request, 'profesores/lista_de_profesores.html', {'profesores': profesores})