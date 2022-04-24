from django.db import models

class estado_perfil(models.Model):
    id = models.BigAutoField(primary_key=True)
    estado = models.CharField(max_length=250, blank=False, null=False)

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estado'
        ordering = ['estado']

    def __str__(self):
        return self.estado

class perfiles_ocupacionales(models.Model):
    id = models.AutoField(primary_key=True)
    universidad = models.CharField(max_length=100, verbose_name='Universidad')
    programa = models.CharField(max_length=100, null=False, verbose_name='Programa')
    perfil = models.TextField(verbose_name='Perfil Ocupacional')
    estado_id = models.ForeignKey(estado_perfil, default=1, on_delete=models.CASCADE, verbose_name='Estado')
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=True, auto_now_add=False)


class historico(models.Model):
    id = models.AutoField(primary_key=True)
    busqueda = models.TextField(verbose_name='Busqueda')
    perfiles = models.CharField(max_length=200, null=False, verbose_name='Perfiles')
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=True, auto_now_add=False)





