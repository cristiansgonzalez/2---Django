from tabnanny import verbose
from django import forms

class formularioComentarios(forms.Form):
    nombreForm = forms.CharField(label = "Usuario",  max_length = 150)
    comentarioForm = forms.CharField(label = "", widget = forms.Textarea(attrs={'placeholder': 'Comentario'}))

class ArchivoExcel(forms.Form):
    file = forms.FileField(label = "excel")
