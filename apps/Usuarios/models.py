from django.db import models
from django.contrib.auth.models import User, AbstractUser

class Rol(models.Model):
    id = models.BigAutoField(primary_key=True)
    rol = models.CharField(max_length=250, blank=False, null=False)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        ordering = ['rol']

    def __str__(self):
        return self.rol

class Tipo(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipo = models.CharField(max_length=250, blank=False, null=False)

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['tipo']

    def __str__(self):
        return self.tipo

class Estado(models.Model):
    id = models.BigAutoField(primary_key=True)
    estado = models.CharField(max_length=250, blank=False, null=False)

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estado'
        ordering = ['estado']

    def __str__(self):
        return self.estado


class CustomUser(User):
    tipo_id = models.ForeignKey(Tipo, on_delete=models.CASCADE, verbose_name='Tipo de persona')




