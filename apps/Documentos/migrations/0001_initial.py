# Generated by Django 3.1 on 2022-04-24 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_documento',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Tipo_Documentos',
                'verbose_name_plural': 'Tipos_Documentos',
                'ordering': ['tipo'],
            },
        ),
        migrations.CreateModel(
            name='archivos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('ruta', models.FileField(upload_to='archivos/', verbose_name='Ruta')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('tipo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Documentos.tipo_documento', verbose_name='Tipo de documento')),
            ],
        ),
    ]
