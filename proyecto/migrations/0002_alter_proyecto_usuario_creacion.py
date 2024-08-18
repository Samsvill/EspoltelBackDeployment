# Generated by Django 5.0.6 on 2024-08-18 03:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='usuario_creacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proyectos', to='user.userprofile'),
        ),
    ]
