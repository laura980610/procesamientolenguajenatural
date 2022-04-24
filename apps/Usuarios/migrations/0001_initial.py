# Generated by Django 3.1 on 2022-02-16 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estado',
                'ordering': ['estado'],
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('rol', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Rol',
                'verbose_name_plural': 'Roles',
                'ordering': ['rol'],
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
                'ordering': ['tipo'],
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido')),
                ('correo', models.EmailField(max_length=200, verbose_name='Correo')),
                ('clave', models.CharField(max_length=100, verbose_name='Contraseña')),
                ('usuario', models.CharField(max_length=100, verbose_name='Usuario')),
                ('estado_id', models.IntegerField(default=3)),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('rol_id', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='Usuarios.rol')),
                ('tipo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuarios.tipo', verbose_name='Tipo de persona')),
            ],
        ),
    ]
