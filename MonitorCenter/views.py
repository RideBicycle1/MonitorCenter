from django.shortcuts import render
# Create your views here.
from MonitorCenter import models
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
    Metrics = models.Metrics.objects.all()
    return render(request, 'MonitorCenter/metric.html', locals())


def sysindex(request):
    """
    系统信息视图
    :param request:
    :return:
    """
    SysInfoManage = models.SysInfoManage.objects.all()
    return render(request, 'MonitorCenter/sysindex.html', locals())
