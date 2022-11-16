from operator import mod
from unittest.util import _MAX_LENGTH
from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length = 150, verbose_name = "Usuario")
    comentario = models.TextField(verbose_name = "Comentario")
    fecha = models.DateField(verbose_name = "Fecha del comentario")

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        db_table = "usuario"

class Video(models.Model):
    title = models.CharField(max_length = 100)
    added = models.DateField(auto_now_add = True)
    url = EmbedVideoField()

    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering = ["-added"]
        verbose_name = "Video"
        verbose_name_plural = "Videos"
        db_table = "video"