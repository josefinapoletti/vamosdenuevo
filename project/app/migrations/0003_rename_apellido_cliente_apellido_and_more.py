# Generated by Django 4.2.1 on 2023-06-02 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_cliente'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='apellido',
            new_name='Apellido',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='nombre',
            new_name='Nombre',
        ),
    ]
