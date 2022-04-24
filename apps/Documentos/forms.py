from django import forms
from .models import archivos

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = archivos
        fields = ['nombre','ruta','tipo_id']