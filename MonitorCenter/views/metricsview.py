from datetime import datetime

from django.http import JsonResponse, Http404
from django.shortcuts import render
# Create your views here.
from MonitorCenter import models
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from MonitorCenter.models import *
from MonitorCenter.serializers import MonitorObjectSerializer, MetricsSerializer, SysInfoManageSerializer, \
    HostsInfoSerializer


class MetricsListCreateView(generics.ListCreateAPIView):
    queryset = Metrics.objects.all()
    serializer_class = MetricsSerializer


class MetricsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Metrics.objects.all()
    serializer_class = MetricsSerializer
    lookup_field = 'id'
    # 添加这一行以允许 DELETE 方法
    http_method_names = ['get', 'put', 'patch', 'delete']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print(instance)
        instance.is_deleted = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_metrics_with_sys_info(request, id, sys_id):
    data = request.data
    sys_id = data.get('sys_id')
    metric_data = {
        'metric_ID': data.get('metric_ID'),
        'metric_name': data.get('metric_name'),
        'metric_type': data.get('metric_type'),
        'metric_desc': data.get('metric_desc'),
        'Threshold': data.get('Threshold'),
        'metric_unit': data.get('metric_unit'),
        'collect_type': data.get('collect_type'),
        'trigger_rule': data.get('trigger_rule'),
    }
    metric_serializer = MetricsSerializer(data=metric_data)
    if metric_serializer.is_valid():
        metric_instance = metric_serializer.save()
        sys_instance = SysInfoManage.objects.get(pk=sys_id)
        MetricsSysInfoManage.objects.create(metric=metric_instance, sys_info=sys_instance)
        return JsonResponse(metric_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(metric_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST'])
# def metrics_list(request):
#     """
#         指标的接口
#         第一个是get返回全部的监控对象信息
#         第二个是post创建数据，如果能保存就返回201，否则返回400
#     """
#     if request.method == 'GET':
#         metrics = Metrics.objects.all()
#         serializer = MetricsSerializer(metrics, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = MetricsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#
# @api_view(['GET', 'POST', 'DELETE'])
# def metrics_detail(request, pk):
#     """
#         指标：
#         判断是否存在返回404
#         get请求返回监控对象信息
#         post请求更新信息，失败返回400
#         删除数据，返回204
#     """
#     try:
#         metric = Metrics.objects.get(pk=pk)
#     except Metrics.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = MetricsSerializer(metric)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = MetricsSerializer(metric, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         metric.delete()
#         return Response(status=status.HTTP_200_OK)


def metric(request):
    """
    监控指标视图
    :param request:
    :return:
    """
    # Metrics = models.Metrics.objects.all()
    sysabb = request.GET.get("sys_abb", "value")
    # 临时加上一个临时值，等后面前端对上了再注释下面临时赋值
    sysabb = "pipeline"
    sysinfo_obj = SysInfoManage.objects.get(Sys_abbreviation=sysabb)
    Metrics = sysinfo_obj.metrics_sys.all()
    return render(request, 'MonitorCenter/metric.html', locals())

#
# def get_sys_metrics(request):
#     """
#     访问带上系统简称字段，字段为系统简称，该接口即可返回该系统下的指标
#     :param request:
#     :return:
#     """
#     if request.method == 'GET':
#         sysabb = request.GET.get("sys_abb", "value")
#         sysinfo_obj = SysInfoManage.objects.get(Sys_abbreviation=sysabb)
#         metrics_obj = sysinfo_obj.metrics_sys.all()
#         serializer = MetricsSerializer(metrics_obj, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#
# def add_sys_metrics(request):
#     """
#     post的数据要以表单形式发起
#     增加指标时调用该接口，可以在系统和指标中间表增加该系统与指标的关联
#     :return:
#     """
#     if request.method == 'POST':
#         sys_id = request.POST.get("sysid", "")
#         metrics_id = request.POST.get("metricsid", "")
#         metrics_obj = Metrics.objects.get(id=metrics_id)
#         sysinfo_obj = SysInfoManage.objects.get(id=sys_id)
#         metrics_obj.metrics_sys.add(sysinfo_obj)
#         serializer = SysInfoManageSerializer(sysinfo_obj)
#         return JsonResponse(serializer.data, safe=False)
