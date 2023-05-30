from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Persona(models.Model):
    name = models.CharField(max_length=50, default='anonymous')
    email = models.EmailField()
    password = models.CharField(max_length=50, default='password.123')
    reparto = models.CharField(max_length=50)

    def __str__(self):
        return self.email
    class Meta:
        verbose_name_plural = 'Persone'
