from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
from MonitorCenter import models
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from MonitorCenter.models import MonitorObject, Metrics, SysInfoManage, HostsInfo
from MonitorCenter.serializers import MonitorObjectSerializer, MetricsSerializer, SysInfoManageSerializer, \
    HostsInfoSerializer


def host_object_list(request):
    """
        主机信息：
        get请求返回主机IP信息
        post发送系统ID以及对象ID以及主机IP信息
        增加主机IP，关联系统和对象
    """
    if request.method == 'GET':
        host_info_detail = HostsInfo.objects.all()
        serializer = HostsInfoSerializer(host_info_detail, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = HostsInfoSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def hostinfo_detail(request, pk):
    """
        指标：
        判断是否存在返回404
        get请求返回监控对象信息
        post请求更新信息，失败返回400
        删除数据，返回204
    """
    try:
        hostinfo = HostsInfo.objects.get(id=pk)
    except Metrics.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HostsInfoSerializer(hostinfo)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HostsInfoSerializer(hostinfo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        hostinfo.delete()
        return Response(status=status.HTTP_200_OK)
