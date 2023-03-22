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
        app_label = 'MonitorCenter'

