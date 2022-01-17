from django.db import models


# Create your models here.

class Animal(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    foto = models.CharField(max_length=100, blank=True, null=True)
    classe = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name_plural = 'Animais'


    def __str__(self):
        return self.nome
