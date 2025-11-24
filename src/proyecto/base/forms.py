from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'completo']
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Título de la tarea'}),
            'descripcion': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Descripción'}),
        }