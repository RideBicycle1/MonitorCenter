from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404

from MonitorCenter import models
from MonitorCenter.models import SysInfoManage
from MonitorCenter.models import MonitorObject

def index(request):
    """
    监控对象视图
    :param request:
    :return:
    """
    MonitorObject = models.MonitorObject.objects.all()
    return render(request, 'MonitorCenter/index.html', locals())


def sysindex(request):
    """
    系统信息视图
    :param request:
    :return:
    """
    SysInfoManage = models.SysInfoManage.objects.all()
    return render(request, 'MonitorCenter/sysindex.html', locals())


"""
创建对象获取系统信息
"""
#for e in SysInfoManage.objects.all():
#    print("测试信息是否能打印")
#    print(e.id)

"""
创建指标
"""
#MonitorObject.objects.create(object_type="operating_system_layer", name="磁盘使用率", object_id="disk", status="1")

"""
创建系统
"""
#SysInfoManage.objects.create(Sys_name="流水线平台", Sys_abbreviation="pipeline", Sys_level="second_level_layer", Sys_dev_pricipal="12313", Sys_ops_pricipal="23332")

"""
给指定系统增加所有公共指标,中间表数据添加
"""
#SysInfoManage.objects.get(Sys_level="second_level_layer").object_id.add(*(MonitorObject.objects.all()))

"""
根据系统的缩写获取该系统下所有指标的信息，待验证
"""
a = SysInfoManage.objects.get(Sys_abbreviation="pipeline").object_id.all()
print(a)
#def more_to_more_select_db(request):
#    # index_list存放满足条件的指标
#    # 查询出“测试项目0309”这个系统的指标
#    index_list = []
#    sysinfo_obj = SysInfoManage.objects.get(Sys_abbreviation="测试项目0309")
#    print(sysinfo_obj)
#    sysinfo_id =
#    index_obj = sysinfo_obj.MonitorObeject.all()
#    for ath in index_obj:
#        index_list.append(ath)
#        print(ath)
#    return HttpResponse("查询结果：%s"%index_list)


