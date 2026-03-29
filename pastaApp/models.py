from django.db import models
from django.contrib.auth.models import User

class Agenda(models.Model):
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contato = models.CharField(max_length=200)
    numero = models.CharField(max_length=20)
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contato

