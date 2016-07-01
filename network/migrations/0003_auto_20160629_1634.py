# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-29 08:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_switchinterface'),
    ]

    operations = [
        migrations.AddField(
            model_name='switch',
            name='cabinet',
            field=models.CharField(default=datetime.datetime(2016, 6, 29, 8, 34, 11, 530000, tzinfo=utc), max_length=256, verbose_name='\u673a\u67dc'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='switch',
            name='position',
            field=models.CharField(max_length=256, verbose_name='\u673a\u4f4d'),
        ),
    ]
