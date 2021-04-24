# form do app música, página onde faço o controle dos campos que aparecem na página de cadastro de músicas

from django import forms  
from musica.models import Musica

class MusicaForm(forms.ModelForm):  
    class Meta:  
        model = Musica  
        fields = ['titulo', 'duracao', 'spotify', 'youtube', 'artista'] 

        widgets = { 'titulo': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'duracao': forms.NumberInput(attrs={ 'class': 'form-control' }),
            'artista': forms.TextInput(attrs={ 'class': 'form-control' }),
      }