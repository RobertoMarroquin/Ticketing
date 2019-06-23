# Generated by Django 2.1.7 on 2019-06-21 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Boleteria', '0006_auto_20190621_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='exhibicion',
            field=models.CharField(choices=[('exh', 'En Exhibicion'), ('prx', 'Proximamente'), ('ina', 'Inactiva')], default='exh', max_length=50, verbose_name='En Exhibicion'),
            preserve_default=False,
        ),
    ]