from django.db import models

# Create your models here.

#criação da classe artista

class Artista(models.Model):  
    nome = models.TextField(max_length=30, null=False, blank=False)
    date_juncao = models.DateField(max_length=100, null=False, blank=False)

    class Meta:  
        db_table = "artista"
