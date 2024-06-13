from django.db import models

# Create your models here.

class Profesor(models.Model):
  nombre = models.CharField(max_length=50)
  apellido = models.CharField(max_length=50)
  email = models.EmailField(max_length=50)
  profesión = models.CharField(max_length=50)
  def __str__(self):
    return f'Nombre: {self.nombre} {self.apellido} --- Email: {self.email} --- Profesión: {self.profesión}'