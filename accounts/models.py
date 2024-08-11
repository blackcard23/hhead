from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.Model):
    nazvaie = models.CharField('Nazvaie', max_length=50)
    nazvaie2 = models.CharField('Nazvaie2', max_length=50)

    def __str__(self):
        return self.nazvaie


class Polzovatel(AbstractUser):
    rol = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.username} - {self.rol}'
