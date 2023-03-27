from django.db import models
from django.contrib.auth.models import User
from .SysInfoManageModel import *
from .MonitorObjectModel import *


class HostsInfo(models.Model):
    ip_address = models.CharField(max_length=64, verbose_name='IP地址')
    sysinfo_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, default=1)
    sysinfo_object_id = models.PositiveIntegerField(default=1)
    sysinfo = GenericForeignKey('sysinfo_content_type', 'sysinfo_object_id')
    obj_id = models.ForeignKey(MonitorObject, on_delete=models.CASCADE, verbose_name="对象模块ID")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_deleted = models.BooleanField(default=False, verbose_name='已删除')

    class Meta:
        verbose_name = '主机IP信息管理'
        verbose_name_plural = '主机IP信息管理'
        ordering = ['-create_time']
        db_table = 'hostinfo'
        app_label = 'MonitorCenter'
