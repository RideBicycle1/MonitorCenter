from django.db import models
from django.contrib.auth.models import User
from .MonitorObjectModel import *


class Metrics(models.Model):
    collect_type = (
        (0, 'Agent'),
        (1, '插件'),
        (2, '协议')
    )
    metrics_type = (
        (0, '系统层级'),
        (1, '自定义'),
        (2, '模块层级')
    )
    trigger_rule_type = (
        ('greater', '>'),
        ('less', '<'),
        ('equal', '='),
        ('unequal', '≠'),
        ('greater_equal', '≥'),
        ('less_equal', '≤')
    )
    # 指标ID，例如：BCLinux-001
    metric_ID = models.CharField(max_length=256, unique=True, verbose_name="监控指标ID")
    # 指标-监控对象
    monitor_object_id = models.ForeignKey(MonitorObject, on_delete=models.CASCADE)
    # 监控指标名称
    metric_name = models.CharField(max_length=64, unique=True, verbose_name='指标名称')
    # 监控指标类型
    metric_type = models.SmallIntegerField(choices=metrics_type, default=0, verbose_name='指标类型')
    # 监控指标描述
    metric_desc = models.CharField(max_length=256, verbose_name='指标描述')
    # 阈值
    Threshold = models.IntegerField(default=0, verbose_name='阈值')
    # 监控指标单位
    metric_unit = models.CharField(max_length=256, verbose_name='指标单位')
    # 监控指标采集类型
    collect_type = models.SmallIntegerField(choices=collect_type, default=0, verbose_name='指标采集类型')
    # 触发规则
    trigger_rule = models.CharField(max_length=256, choices=trigger_rule_type, default='less', verbose_name='触发规则')
    # 指标创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    # 指标更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')
    # 指标与系统之间的多对多
    metrics_sys = models.ManyToManyField("SysInfoManage", related_name='metrics_sys')

    def __str__(self):
        return '<%s>  %s' % (self.get_collect_type_display(), self.collect_type)

    def __str__(self):
        return '<%s>  %s' % (self.get_trigger_rule_display(), self.collect_type)

    class Meta:
        verbose_name = '监控指标表'
        verbose_name_plural = '监控指标表'
        ordering = ['-create_time']
        db_table = 'metrics'
        app_label = 'MonitorCenter'

