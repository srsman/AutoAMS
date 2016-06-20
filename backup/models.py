# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from idcroom.models import Idcroom
from collections import OrderedDict


class Serverbk(models.Model):
    sn = models.CharField('序列号',max_length=256)
    brand = models.CharField('品牌',max_length=256)
    model = models.CharField('型号',max_length=256)
    cpu = models.TextField('CPU',default='') # json格式存储
    memory = models.TextField('内存',default='') # json格式存储
    disk = models.TextField('硬盘',default='') # json格式存储
    idcroom = models.ForeignKey(Idcroom,verbose_name='所在机房')
    user = models.CharField('操作员',max_length=256)
    comment = models.TextField('备注',default='')
    guarantee = models.CharField('保修年限',max_length=256)
    buydate = models.CharField('购买日期',max_length=256)
    uptime = models.DateTimeField('更新时间',auto_now=True,null=True)

class Diskbk(models.Model):
    # 状态，OrderedDict保持字典原来顺序
    STATUS = OrderedDict([
        ('backup','备件'),
        ('fault','故障'),
        ('scrap','报废'),
    ])
    sn = models.CharField('序列号',max_length=256)
    brand = models.CharField('品牌',max_length=256)
    type = models.CharField('类型',max_length=256)
    capacity = models.CharField('容量',max_length=256)
    status = models.CharField('状态',max_length=10,default='backup')
    idcroom = models.ForeignKey(Idcroom,verbose_name='所在机房')
    user = models.CharField('操作员',max_length=256)
    comment = models.TextField('备注',default='')
    guarantee = models.CharField('保修年限',max_length=256)
    buydate = models.CharField('购买日期',max_length=256)
    uptime = models.DateTimeField('更新时间',auto_now=True,null=True)

class Memorybk(models.Model):
    # 状态，OrderedDict保持字典原来顺序
    STATUS = OrderedDict([
        ('backup','备件'),
        ('fault','故障'),
        ('scrap','报废'),
    ])
    sn = models.CharField('序列号',max_length=256)
    brand = models.CharField('品牌',max_length=256)
    type = models.CharField('类型',max_length=256)
    capacity = models.CharField('容量',max_length=256)
    status = models.CharField('状态',max_length=10,default='backup')
    idcroom = models.ForeignKey(Idcroom,verbose_name='所在机房')
    user = models.CharField('操作员',max_length=256)
    comment = models.TextField('备注',default='')
    guarantee = models.CharField('保修年限',max_length=256)
    buydate = models.CharField('购买日期',max_length=256)
    uptime = models.DateTimeField('更新时间',auto_now=True,null=True)
