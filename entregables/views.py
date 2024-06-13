from django.shortcuts import render

# Create your views here.
def entregables(request):
  return render(request, 'entregables.html')