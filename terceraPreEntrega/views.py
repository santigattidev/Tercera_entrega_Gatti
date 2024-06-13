from django.shortcuts import render

def inicio_index(request):
  return render(request, 'inicioIndex.html')