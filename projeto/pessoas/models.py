from django.db import models
from django.contrib.auth.models import AbstractUser

class Pessoa (models.Model):
	nome = models.CharField( max_length=100)
	email = models.EmailField()
	ativo = models.BooleanField(default=True)
	data_nascimento = models.DateField()


class Login(AbstractUser):
	endereco = models.CharField(max_length=100, blank=True, null=True)
