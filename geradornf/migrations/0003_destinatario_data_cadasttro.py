# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-30 15:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('geradornf', '0002_auto_20160723_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='destinatario',
            name='data_cadasttro',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 7, 30, 15, 45, 31, 685882, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
