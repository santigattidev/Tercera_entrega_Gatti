from django import forms

class CrearCurso(forms.Form):
  nombre = forms.CharField(max_length=50)
  camada = forms.IntegerField()