# Generated by Django 4.0.6 on 2022-08-07 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorias',
            name='id_producto',
        ),
    ]
