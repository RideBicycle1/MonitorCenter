from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
from MonitorCenter import models
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from MonitorCenter.models import MonitorObject, Metrics, SysInfoManage, HostsInfo
from MonitorCenter.serializers import MonitorObjectSerializer, MetricsSerializer, SysInfoManageSerializer, HostsInfoSerializer

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
        return Response(status=status.HTTP_200_OK)


def index(request):
    """
    监控对象视图.首页获取信息
    :param request:
    :return:
    """
    MonitorObject = models.MonitorObject.objects.all()
    return render(request, 'MonitorCenter/index.html', locals())

