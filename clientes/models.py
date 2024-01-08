from django.db import models

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=30)
    sobrenome = models.CharField('Sobrenome', max_length=30)

