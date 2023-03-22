from django.db import models
from django.contrib.auth.models import User
from .SysInfoManageModel import *
from .MonitorObjectModel import *


class HostsInfo(models.Model):
    ip_address = models.CharField(max_length=64, verbose_name='IP地址')
    sys_id = models.ForeignKey(SysInfoManage, on_delete=models.CASCADE, verbose_name="系统ID")
    obj_id = models.ForeignKey(MonitorObject, on_delete=models.CASCADE, verbose_name="对象模块ID")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '主机IP信息管理'
        verbose_name_plural = '主机IP信息管理'
        ordering = ['-create_time']
        db_table = 'hostinfo'
        app_label = 'MonitorCenter'
