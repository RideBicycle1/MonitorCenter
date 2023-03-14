from django.contrib import admin

# Register your models here.
from .models import MonitorObject, Metrics, SysInfoManage


class MonitorObjectAdmin(admin.ModelAdmin):
    list_display = ('object_type', 'object_name', 'create_time', 'update_time')

    '''过滤字段'''
    list_filter = ('create_time',)

    '''分页大小：10'''
    list_per_page = 10


class MetricsAdmin(admin.ModelAdmin):
    list_display = ('metric_ID', 'monitor_object_id', 'metric_name', 'metric_type', 'metric_desc'
                    , 'metric_unit', 'collect_type', 'create_time', 'update_time')

    '''过滤字段'''
    list_filter = ('create_time',)

    '''分页大小：10'''
    list_per_page = 10

class SysInfoManageAdmin(admin.ModelAdmin):
    list_display = ('Sys_name', 'Sys_abbreviation', 'Sys_level', 'Sys_dev_pricipal', 'Sys_ops_pricipal'
                    , 'create_time', 'update_time')

    '''过滤字段'''
    list_filter = ('create_time',)

    '''分页大小：10'''
    list_per_page = 10

admin.site.register(MonitorObject, MonitorObjectAdmin)
admin.site.register(Metrics, MetricsAdmin)
admin.site.register(SysInfoManage, SysInfoManageAdmin)
