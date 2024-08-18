# Generated by Django 5.0.6 on 2024-08-18 02:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proyecto', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('proveedor', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('no_coti', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('url_coti', models.URLField(blank=True, default=None, null=True)),
                ('fecha_coti', models.DateField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'Cotización',
                'verbose_name_plural': 'Cotizaciones',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('mensaje', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=18)),
                ('nombre', models.CharField(max_length=200)),
                ('tema', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('cotizacion_aceptada', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='solicitudes', to='solicitud.cotizacion')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes', to='solicitud.estado')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes', to='proyecto.proyecto')),
                ('usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes', to='user.userprofile')),
                ('usuario_modificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes_modificadas', to='user.userprofile')),
            ],
            options={
                'verbose_name': 'Solicitud',
                'verbose_name_plural': 'Solicitudes',
                'ordering': ['-fecha_creacion'],
            },
        ),
        migrations.CreateModel(
            name='ItemSolicitud',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=200)),
                ('cantidad', models.IntegerField()),
                ('unidad', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='proyecto.budgetitem')),
                ('solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='solicitud.solicitud')),
            ],
            options={
                'verbose_name': 'Item solicitud',
                'verbose_name_plural': 'Items solicitud',
            },
        ),
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cedula_ruc', models.CharField(max_length=13)),
                ('tipo_compra', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('no_compra', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('url_compra', models.URLField(blank=True, default=None, null=True)),
                ('tipo_acuerdo', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('forma_pago', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('tipo_pago', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('tiempo', models.SmallIntegerField(blank=True, default=None, null=True)),
                ('url_certi_banco', models.URLField(blank=True, default=None, null=True)),
                ('anticipo', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True)),
                ('nombre_banco', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('tipo_cuenta', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('numero_cuenta', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('nombre_cuenta', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('correo', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='formulario', to='solicitud.solicitud')),
            ],
            options={
                'verbose_name': 'Formulario',
                'verbose_name_plural': 'Formularios',
            },
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=100)),
                ('monto', models.DecimalField(decimal_places=5, max_digits=10)),
                ('comentario', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='factura', to='solicitud.solicitud')),
            ],
            options={
                'verbose_name': 'Factura',
                'verbose_name_plural': 'Facturas',
            },
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='solicitud',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cotizacion', to='solicitud.solicitud'),
        ),
    ]
