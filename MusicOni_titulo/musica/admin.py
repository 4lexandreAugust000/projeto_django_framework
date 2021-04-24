# o admin do django tem acesso aos apps musica e artista

#criei um admin com o user: musica_artista, senha: senhadoadmin, estou informando pois não sei como o projeto funciona em outros computadores

from django.contrib import admin
from musica.models import Musica
from artista.models import Artista

admin.site.register(Musica)
admin.site.register(Artista)