from django.contrib import admin

from .models import MonitorObject
from .models import SysInfoManage


admin.site.register(MonitorObject)
admin.site.register(SysInfoManage)

# Register your models here.

