# Generated by Django 5.0 on 2024-01-27 03:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_page_id_alter_page_image'),
        ('vehiculo', '0005_alter_rent_fecha_devolucion_alter_rent_fecha_renta'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent',
            name='apellido',
            field=models.CharField(default='', max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rent',
            name='cedula',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rent',
            name='nombre',
            field=models.CharField(default='', max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rent',
            name='telefono',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rent',
            name='tipo_vehiculo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pages.page'),
        ),
    ]
