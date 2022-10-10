from operator import mod
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length = 150, verbose_name = "Usuario")
    comentario = models.TextField(verbose_name = "Comentario")
    fecha = models.DateField(verbose_name = "Fecha del comentario")

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        db_table = "usuario"