# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-01 03:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_auto_20160701_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='server',
            name='other_ip',
        ),
        migrations.AddField(
            model_name='server',
            name='all_ip',
            field=models.CharField(default='', max_length=256, verbose_name='\u5168\u90e8ip'),
        ),
    ]
