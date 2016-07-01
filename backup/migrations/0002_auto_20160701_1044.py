# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-01 02:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diskbk',
            name='brand',
            field=models.CharField(default='', max_length=256, verbose_name='\u54c1\u724c'),
        ),
        migrations.AlterField(
            model_name='diskbk',
            name='buydate',
            field=models.CharField(default='', max_length=256, verbose_name='\u8d2d\u4e70\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='diskbk',
            name='capacity',
            field=models.CharField(default='', max_length=256, verbose_name='\u5bb9\u91cf'),
        ),
        migrations.AlterField(
            model_name='diskbk',
            name='guarantee',
            field=models.CharField(default='', max_length=256, verbose_name='\u4fdd\u4fee\u5e74\u9650'),
        ),
        migrations.AlterField(
            model_name='diskbk',
            name='idcroom',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='idcroom.Idcroom', verbose_name='\u6240\u5728\u673a\u623f'),
        ),
        migrations.AlterField(
            model_name='diskbk',
            name='sn',
            field=models.CharField(default='', max_length=256, verbose_name='\u5e8f\u5217\u53f7'),
        ),
        migrations.AlterField(
            model_name='diskbk',
            name='type',
            field=models.CharField(default='', max_length=256, verbose_name='\u7c7b\u578b'),
        ),
        migrations.AlterField(
            model_name='diskbk',
            name='user',
            field=models.CharField(default='', max_length=256, verbose_name='\u64cd\u4f5c\u5458'),
        ),
        migrations.AlterField(
            model_name='memorybk',
            name='brand',
            field=models.CharField(default='', max_length=256, verbose_name='\u54c1\u724c'),
        ),
        migrations.AlterField(
            model_name='memorybk',
            name='buydate',
            field=models.CharField(default='', max_length=256, verbose_name='\u8d2d\u4e70\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='memorybk',
            name='capacity',
            field=models.CharField(default='', max_length=256, verbose_name='\u5bb9\u91cf'),
        ),
        migrations.AlterField(
            model_name='memorybk',
            name='guarantee',
            field=models.CharField(default='', max_length=256, verbose_name='\u4fdd\u4fee\u5e74\u9650'),
        ),
        migrations.AlterField(
            model_name='memorybk',
            name='idcroom',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='idcroom.Idcroom', verbose_name='\u6240\u5728\u673a\u623f'),
        ),
        migrations.AlterField(
            model_name='memorybk',
            name='sn',
            field=models.CharField(default='', max_length=256, verbose_name='\u5e8f\u5217\u53f7'),
        ),
        migrations.AlterField(
            model_name='memorybk',
            name='type',
            field=models.CharField(default='', max_length=256, verbose_name='\u7c7b\u578b'),
        ),
        migrations.AlterField(
            model_name='memorybk',
            name='user',
            field=models.CharField(default='', max_length=256, verbose_name='\u64cd\u4f5c\u5458'),
        ),
        migrations.AlterField(
            model_name='serverbk',
            name='brand',
            field=models.CharField(default='', max_length=256, verbose_name='\u54c1\u724c'),
        ),
        migrations.AlterField(
            model_name='serverbk',
            name='buydate',
            field=models.CharField(default='', max_length=256, verbose_name='\u8d2d\u4e70\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='serverbk',
            name='guarantee',
            field=models.CharField(default='', max_length=256, verbose_name='\u4fdd\u4fee\u5e74\u9650'),
        ),
        migrations.AlterField(
            model_name='serverbk',
            name='idcroom',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='idcroom.Idcroom', verbose_name='\u6240\u5728\u673a\u623f'),
        ),
        migrations.AlterField(
            model_name='serverbk',
            name='model',
            field=models.CharField(default='', max_length=256, verbose_name='\u578b\u53f7'),
        ),
        migrations.AlterField(
            model_name='serverbk',
            name='sn',
            field=models.CharField(default='', max_length=256, verbose_name='\u5e8f\u5217\u53f7'),
        ),
        migrations.AlterField(
            model_name='serverbk',
            name='user',
            field=models.CharField(default='', max_length=256, verbose_name='\u64cd\u4f5c\u5458'),
        ),
    ]
