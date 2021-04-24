# form do app artista, esse form só está visivel no admin do django, pode criar um objeto artista lá ou no banco de dados

from django import forms  
from artista.models import Artista
from artista.models import Artista

class ArtistaForm(forms.ModelForm):  
    class Meta:  
        model = Artista  
        fields = ['nome', 'date_juncao'] 

        widgets = { 'nome': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'date_juncao': forms.TextInput(attrs={ 'class': 'form-control' }),
      }
