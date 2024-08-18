# Generated by Django 5.0.6 on 2024-08-18 02:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200, unique=True)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('project_budget', models.IntegerField()),
                ('usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proyectos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-fecha_creacion'],
            },
        ),
        migrations.CreateModel(
            name='BudgetItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recurso', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField()),
                ('valor', models.FloatField()),
                ('presupuesto', models.FloatField(default=0.0)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='budget_items', to='proyecto.proyecto')),
            ],
        ),
    ]
