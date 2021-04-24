from django.db import models

# Create your models here.


#criação das classes musica e login do artista

class Musica(models.Model):  

    SPOTIFY_CHOICES = (
        ("SIM", "Já foi publicado"),
        ("NÃO", "Não foi publicado")
    )

    YOUTUBE_CHOICES = (
        ("SIM", "Já foi publicado"),
        ("NÃO", "Não foi publicado")
    )

    titulo = models.TextField(max_length=50, null=False, blank=False)
    duracao = models.TextField(max_length=100, null=False, blank=False)
    spotify = models.CharField(max_length=3, choices=SPOTIFY_CHOICES, blank=False, null=False)
    youtube = models.CharField(max_length=3, choices=YOUTUBE_CHOICES, blank=False, null=False)
    artista = models.TextField(max_length=100, null=False, blank=False)

    class Meta:  
        db_table = "musica"

class Login_artista(models.Model):
    nome=models.CharField(max_length=30)
    sobrenome=models.CharField(max_length=30)
    usuario=models.CharField(max_length=30)
    senha=models.CharField(max_length=12)

    def __str__(self):
        return self.nome + " " + self.sobrenome
  
 
    class Meta:  
        db_table = "login_artista"

    