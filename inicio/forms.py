from django import forms

class BuscarCurso(forms.Form):
  nombre = forms.CharField(max_length=50, required=False)