# Generated by Django 2.1.7 on 2019-06-19 22:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Facturacion', '0011_auto_20190619_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='codigoCompra',
            field=models.CharField(default=uuid.UUID('fcbb93e5-4ab9-4d79-96df-7a3ead564c5b'), editable=False, max_length=40),
        ),
    ]