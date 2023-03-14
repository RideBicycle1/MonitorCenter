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
    # 监控对象类型
    object_type = models.CharField(choices=object_layer, max_length=64, default='hardware_device_layer',
                                   verbose_name="监控对象层级")
    # 监控对象名称
    object_name = models.CharField(max_length=64, verbose_name='监控对象名称')
    # 监控对象创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    # 监控对象更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')

    def __str__(self):
        return '<%s>  %s' % (self.get_object_type_display(), self.object_name)

    class Meta:
        verbose_name = '监控对象表'
        verbose_name_plural = '监控对象表'
        ordering = ['-create_time']
        db_table = 'monitorobject'


class Metrics(models.Model):
    type = (
        (0, 'Agent'),
        (1, '插件'),
        (2, '协议')
    )

    # 指标ID，例如：BCLinux-001
    metric_ID = models.CharField(max_length=256, unique=True, verbose_name="监控指标ID")
    # 指标-监控对象
    monitor_object_id = models.ForeignKey(MonitorObject, on_delete=models.CASCADE)
    # 监控指标名称
    metric_name = models.CharField(max_length=64, unique=True, verbose_name='指标名称')
    # 监控指标类型?????为啥唯一
    metric_type = models.CharField(max_length=64, verbose_name='指标类型')
    # 监控指标描述
    metric_desc = models.CharField(max_length=256, verbose_name='指标描述')
    # 监控指标单位
    metric_unit = models.CharField(max_length=256, verbose_name='指标单位')
    # 监控指标采集类型
    collect_type = models.SmallIntegerField(choices=type, default=0, verbose_name='指标采集类型')
    # 指标创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    # 指标更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')

    def __str__(self):
        return '<%s>  %s' % (self.get_collect_type_display(), self.collect_type)

    class Meta:
        verbose_name = '监控指标表'
        verbose_name_plural = '监控指标表'
        ordering = ['-create_time']
        db_table = 'metrics'


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
    metrics_id = models.ManyToManyField(to=Metrics, through='SysinfoMetrics', through_fields=('sysinfo_id', 'metrics_id'))
    mobject_id = models.ManyToManyField(to=MonitorObject)


    def __str__(self):
        return '<%s>  %s' % (self.get_Sys_level_display(), self.Sys_level)

    class Meta:
        verbose_name = '系统信息管理'
        verbose_name_plural = '系统信息管理'
        ordering = ['-create_time']
        db_table = 'sysinfomanage'


class SysinfoMetrics(models.Model):
    metrics_status = (
        (0, '停用'),
        (1, '启用'),
    )
    sysinfo_id = models.ForeignKey(to='SysInfoManage', on_delete=models.CASCADE)
    metrics_id = models.ForeignKey(to="Metrics", on_delete=models.CASCADE)
    status = models.SmallIntegerField(choices=metrics_status, default=0, verbose_name='监控指标启停状态')

    def __str__(self):
        return '<%s>  %s' % (self.get_metrics_status_display(), self.status)

    class Meta:
        verbose_name = '系统与指标关联表'
        db_table = 'sysinfometrics'
