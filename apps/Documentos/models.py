from django.db import models

class Tipo_documento(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipo = models.CharField(max_length=250, blank=False, null=False)

    class Meta:
        verbose_name = 'Tipo_Documentos'
        verbose_name_plural = 'Tipos_Documentos'
        ordering = ['tipo']

    def __str__(self):
        return self.tipo




class archivos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    ruta = models.FileField(upload_to='archivos/', verbose_name='Ruta')
    tipo_id = models.ForeignKey(Tipo_documento, on_delete=models.CASCADE, verbose_name='Tipo de documento')
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=True, auto_now_add=False)
