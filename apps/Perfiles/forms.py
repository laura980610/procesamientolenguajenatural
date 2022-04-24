from django import forms
from .models import perfiles_ocupacionales, historico

class PerfilesForm(forms.ModelForm):
    class Meta:
        model = perfiles_ocupacionales
        fields = ['universidad','programa','perfil']

class FiltroBusqueda():
    class Meta:
        fields = ['filtro']

class HistoricoForm(forms.ModelForm):
    class Meta:
        model = historico
        fields = ['busqueda','perfiles']