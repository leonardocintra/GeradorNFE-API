# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-30 20:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geradornf', '0006_transportadorcontrato'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destinatario',
            old_name='data_cadasttro',
            new_name='data_cadastro',
        ),
        migrations.RenameField(
            model_name='emitente',
            old_name='data_cadasttro',
            new_name='data_cadastro',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='data_cadasttro',
            new_name='data_cadastro',
        ),
        migrations.RenameField(
            model_name='transportador',
            old_name='data_cadasttro',
            new_name='data_cadastro',
        ),
    ]
