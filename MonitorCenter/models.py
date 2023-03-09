from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class MonitorObject(models.Model):
    """
        监控对象层级：hardware_device_layer(硬件设备层)、operating_system_layer(操作系统层)、component_service_layer(组件服务层)、application_performance_layer(应用性能层)
        """
    object_layer = (
        ('hardware_device_layer', '硬件设备层'),
        ('operating_system_layer', '操作系统层'),
        ('component_service_layer', '组件服务层'),
        ('application_performance_layer', '应用性能层'),
    )
    object_status = (
        (0, '停用'),
        (1, '启用'),
    )
    object_type = models.CharField(choices=object_layer, max_length=64, default='hardware_device_layer',
                                   verbose_name="监控对象层级")
    name = models.CharField(max_length=64, unique=True, verbose_name='监控对象名称')
    object_id = models.CharField(max_length=64, unique=True, verbose_name='监控对象对应监控指标id')
    status = models.SmallIntegerField(choices=object_status, default=0, verbose_name='监控对象启停状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')

    def __str__(self):
        return '<%s>  %s' % (self.get_object_type_display(), self.name)

    class Meta:
        verbose_name = '监控对象表'
        verbose_name_plural = '监控对象表'
        ordering = ['-create_time']


class SysInfoManage(models.Model):
    sys_level_layer = (
        ('first_level_layer', '一级系统'),
        ('second_level_layer', '二级系统'),
        ('third_level_layer', '三级系统'),
    )
    Sys_name = models.CharField(max_length=64, verbose_name='系统全称')
    Sys_abbreviation = models.CharField(max_length=64, verbose_name='系统简称')
    Sys_level = models.CharField(choices=sys_level_layer, max_length=64, unique=True, default='third_level_layer',
                                 verbose_name='系统等级')
    Sys_dev_pricipal = models.CharField(max_length=32, verbose_name='系统开发负责人')
    Sys_ops_pricipal = models.CharField(max_length=32, verbose_name='系统运维负责人')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    object_id = models.ManyToManyField(to=MonitorObject)

    def __str__(self):
        return '<%s>  %s' % (self.get_Sys_level_display(), self.Sys_name)

    class Meta:
        verbose_name = '系统信息管理'
        verbose_name_plural = '系统信息管理'
        ordering = ['-create_time']
