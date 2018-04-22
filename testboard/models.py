from django.db import models
from jsonfield import JSONField
from versatileimagefield.fields import (
    PPOIField, VersatileImageField
)

class Machine(models.Model):
    '''
    机器

    + ppoi字段没有实际意义，只是为了配合图片插件使用
    '''

    MACHINE_TYPES = (
        (0, 'TYPE 0'),
        (1, 'TYPE 1'),
        (2, 'TYPE 2')
    )

    no = models.CharField(null=True, blank=True, max_length=50, verbose_name='编号')
    type = models.SmallIntegerField(null=True, blank=True, choices=MACHINE_TYPES, verbose_name='型号')
    ppoi = PPOIField(null=True, blank=True, verbose_name='关键点')
    qr = VersatileImageField(null=True, blank=True, upload_to='qr', ppoi_field='ppoi', verbose_name='二维码')

    class Meta:
        db_table = 'machine'
        verbose_name = '机器'
        verbose_name_plural = '机器'

    def __str__(self):
        return self.no


class Touch(models.Model):
    '''
    触点

    + 对特定参数的测量总是成对出现，只是类型不同
    + 若针对触点进行测量，且测量结果有八个数据，可扩展此表实现
    '''

    RECORD_TYPES = (
        (0, '电压'),
        (1, '电流'),
        (2, '电阻'),
        (3, '时间')
    )

    close = JSONField(null=True, blank=True, verbose_name='闭合')
    open = JSONField(null=True, blank=True, verbose_name='释放')
    type = models.SmallIntegerField(null=True, blank=True, choices=RECORD_TYPES, verbose_name='类型')
    time_joined = models.DateTimeField(auto_now_add=True, verbose_name='测量时间')
    machine = models.CharField(null=True, blank=True, max_length=50, verbose_name='机器')

    class Meta:
        db_table = 'touch'
        verbose_name = '触点测试'
        verbose_name_plural = '触点测试'


class Relay(models.Model):
    '''
    继电器

    + 对特定参数的测量总是成对出现，只是类型不同
    + 若对继电器进行测量，测量结果只有一个数据，可扩展此表实现
    '''

    RECORD_TYPES = (
        (0, '电压'),
        (1, '电流'),
        (2, '电阻'),
        (3, '时间')
    )

    close = models.FloatField(null=True, blank=True, verbose_name='闭合')
    open = models.FloatField(null=True, blank=True, verbose_name='释放')
    type = models.SmallIntegerField(null=True, blank=True, choices=RECORD_TYPES, verbose_name='类型')
    time_joined = models.DateTimeField(auto_now_add=True, verbose_name='测量时间')
    machine = models.CharField(null=True, blank=True, max_length=50, verbose_name='机器', db_index=True)

    class Meta:
        db_table = 'relay'
        verbose_name = '继电器测试'
        verbose_name_plural = '继电器测试'