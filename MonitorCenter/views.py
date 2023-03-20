from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.utils import json

# Create your views here.
from MonitorCenter import models
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .models import MonitorObject, Metrics, SysInfoManage
from .serializers import MonitorObjectSerializer, MetricsSerializer, SysInfoManageSerializer



@api_view(['GET', 'POST'])
def monitor_object_list(request):
    """
        监控对象的接口
        第一个是get返回全部的监控对象信息
        第二个是post创建数据，如果能保存就返回201，否则返回400
    """
    if request.method == 'GET':
        monitor_objects = MonitorObject.objects.all()
        serializer = MonitorObjectSerializer(monitor_objects, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MonitorObjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def metrics_list(request):
    """
        指标的接口
        第一个是get返回全部的监控对象信息
        第二个是post创建数据，如果能保存就返回201，否则返回400
    """
    if request.method == 'GET':
        metrics = Metrics.objects.all()
        serializer = MetricsSerializer(metrics, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MetricsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def sysinfo_object_list(request):
    """
        监控对象的接口
        第一个是get返回全部的监控对象信息
        第二个是post创建数据，如果能保存就返回201，否则返回400
    """
    if request.method == 'GET':
        sysinfo_objects = SysInfoManage.objects.all()
        serializer = SysInfoManageSerializer(sysinfo_objects, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SysInfoManageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def monitor_object_detail(request, pk):
    """
        监控对象：
        判断是否存在返回404
        get请求返回监控对象信息
        post请求更新信息，失败返回400
        删除数据，返回204
    """
    try:
        monitor_object = MonitorObject.objects.get(pk=pk)
    except MonitorObject.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MonitorObjectSerializer(monitor_object)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MonitorObjectSerializer(monitor_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        monitor_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def login(request):
    # 先定义出返回数据的格式
    res = {"code": 20000, "data": None, 'data': "success"}
    # 添加返回的数据
    # 返回
    return HttpResponse(json.dumps(res))

@api_view(['GET'])
def info(request):
    # 先定义出返回数据的格式
    res = {"code": 20000, "data": 'admin'}
    # 添加返回的数据
    # 返回
    return HttpResponse(json.dumps(res))

@api_view(['GET', 'POST', 'DELETE'])
def metrics_detail(request, pk):
    """
        指标：
        判断是否存在返回404
        get请求返回监控对象信息
        post请求更新信息，失败返回400
        删除数据，返回204
    """
    try:
        metric = Metrics.objects.get(pk=pk)
    except Metrics.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MetricsSerializer(metric)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MetricsSerializer(metric, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        metric.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def sysinfo_object_detail(request, pk):
    """
        系统信息：
        判断是否存在返回404
        get请求返回监控对象信息
        post请求更新信息，失败返回400
        删除数据，返回204
    """
    try:
        sysinfo_object = SysInfoManage.objects.get(pk=pk)
    except SysInfoManage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SysInfoManageSerializer(sysinfo_object)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SysInfoManageSerializer(sysinfo_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        sysinfo_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def index(request):
    """
    监控对象视图.首页获取信息
    :param request:
    :return:
    """
    MonitorObject = models.MonitorObject.objects.all()
    return render(request, 'MonitorCenter/index.html', locals())


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


def sysindex(request):
    """
    系统信息视图
    :param request:
    :return:
    """
    SysInfoManage = models.SysInfoManage.objects.all()
    return render(request, 'MonitorCenter/sysindex.html', locals())


def get_sys_metrics(request):
    """
    访问带上字段，字段为系统简称，该接口即可返回该系统下的指标
    :param request:
    :return:
    """
    if request.method == 'GET':
        sysabb = request.GET.get("sys_abb", "value")
        sysinfo_obj = SysInfoManage.objects.get(Sys_abbreviation=sysabb)
        metrics_obj = sysinfo_obj.metrics_sys.all()
        serializer = MetricsSerializer(metrics_obj, many=True)
        return JsonResponse(serializer.data, safe=False)


def add_sys_metrics(request):
    """
    post的数据要以表单形式发起
    增加指标时调用该接口，可以在系统和指标中间表增加该系统与指标的关联
    :return:
    """
    if request.method == 'POST':
        sys_id = request.POST.get("sysid", "")
        metrics_id = request.POST.get("metricsid", "")
        metrics_obj = Metrics.objects.get(id=metrics_id)
        sysinfo_obj = SysInfoManage.objects.get(id=sys_id)
        sysinfo_obj.metrics_sys.add(metrics_obj)
        serializer = MetricsSerializer(metrics_obj)
        return JsonResponse(serializer.data, safe=False)
