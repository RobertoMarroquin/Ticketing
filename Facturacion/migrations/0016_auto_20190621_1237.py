# Generated by Django 2.1.7 on 2019-06-21 18:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Facturacion', '0015_auto_20190621_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='codigoCompra',
            field=models.CharField(default=uuid.UUID('3aa38fdf-1b01-4d74-aa74-2c3979ae95a5'), editable=False, max_length=40),
        ),
    ]
