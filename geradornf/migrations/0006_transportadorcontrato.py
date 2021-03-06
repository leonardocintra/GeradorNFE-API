# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-30 16:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geradornf', '0005_produto_transportador'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransportadorContrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_servico', models.DecimalField(decimal_places=2, max_digits=9)),
                ('valor_base', models.DecimalField(decimal_places=2, max_digits=9)),
                ('aliquota', models.DecimalField(decimal_places=2, max_digits=9)),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=9)),
                ('CFOP', models.CharField(blank=True, max_length=50, null=True)),
                ('cidade_codigo_placa', models.IntegerField(blank=True, null=True)),
                ('RNTC', models.CharField(blank=True, max_length=50, null=True)),
                ('transportador_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geradornf.Transportador')),
            ],
        ),
    ]
