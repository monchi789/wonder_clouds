# Generated by Django 5.0.4 on 2024-04-26 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_proyectos'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Proyectos',
        ),
    ]