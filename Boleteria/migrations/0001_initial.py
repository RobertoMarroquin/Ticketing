# Generated by Django 2.1.7 on 2019-06-05 19:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boleteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('eslogan', models.CharField(blank=True, max_length=100)),
                ('logo', models.ImageField(height_field=400, upload_to='imagenes/', width_field=400)),
            ],
        ),
        migrations.CreateModel(
            name='Boleto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_cliente', models.CharField(blank=True, max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Butaca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_asiento', models.IntegerField(blank=True, null=True)),
                ('fila', models.CharField(blank=True, max_length=2)),
                ('disponibilidad', models.BooleanField(default=True)),
                ('clase', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Funcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.TimeField(blank=True)),
                ('fecha', models.DateField(default=datetime.datetime.today)),
                ('lenguaje', models.CharField(blank=True, max_length=100)),
                ('formato', models.CharField(blank=True, max_length=100)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('pais', models.CharField(blank=True, max_length=100)),
                ('anyo', models.IntegerField(blank=True, null=True)),
                ('duracion', models.IntegerField(blank=True, null=True)),
                ('sinopsis', models.TextField(blank=True)),
                ('clasificacion', models.CharField(blank=True, max_length=2)),
                ('genero', models.CharField(blank=True, max_length=100)),
                ('imagen', models.ImageField(height_field=400, upload_to='peliculas', width_field=400)),
                ('boleteria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Boleteria.Boleteria')),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('numero_sala', models.IntegerField(blank=True, null=True)),
                ('numero_asientos', models.IntegerField(blank=True, null=True)),
                ('numero_filas', models.IntegerField(blank=True, null=True)),
                ('numero_columnas', models.IntegerField(blank=True, null=True)),
                ('clase', models.CharField(blank=True, max_length=100)),
                ('boleteria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Boleteria.Boleteria')),
            ],
        ),
        migrations.AddField(
            model_name='funcion',
            name='pelicula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Boleteria.Pelicula'),
        ),
        migrations.AddField(
            model_name='funcion',
            name='sala',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Boleteria.Sala'),
        ),
        migrations.AddField(
            model_name='butaca',
            name='Sala',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Boleteria.Sala'),
        ),
        migrations.AddField(
            model_name='boleto',
            name='Funcion',
            field=models.ManyToManyField(to='Boleteria.Funcion'),
        ),
    ]