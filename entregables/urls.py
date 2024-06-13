from django.urls import path
from . import views

urlpatterns = [
  path('entregables/', views.entregables, name='entregables'),
]