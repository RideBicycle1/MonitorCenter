from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, QueryDict
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.utils import json

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
    if request.method == 'POST':
        # 创建主机记录
        serializer = HostsInfoSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status': 'success', 'host': serializer.data})
        else:
            return JsonResponse({'status': 'error', 'errors': serializer.errors})

    if request.method == 'GET':
        # 查询主机记录
        sysinfo = request.GET.get('sysinfo')
        obj_id = request.GET.get('obj_id')
        queryset = HostsInfo.objects.filter(is_deleted=False)
        if sysinfo:
            queryset = queryset.filter(sysinfo=sysinfo)
        if obj_id:
            queryset = queryset.filter(obj_id=obj_id)
        serializer = HostsInfoSerializer(queryset, many=True)
        return JsonResponse({'status': 'success', 'hosts': serializer.data})


@api_view(['GET', 'PATCH', 'DELETE'])
def host_object_detail(request, host_id):
    if request.method == 'GET':
        # 查询指定ID的主机记录
        try:
            host = HostsInfo.objects.get(id=host_id, is_deleted=False)
            serializer = HostsInfoSerializer(host)
            return JsonResponse({'status': 'success', 'host': serializer.data})
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Host not found'})

    elif request.method == 'PATCH':
        # 更新主机记录
        data = json.loads(request.body)
        try:
            host = HostsInfo.objects.get(id=host_id)
            serializer = HostsInfoSerializer(host, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                print(serializer.data)
                return JsonResponse({'status': 'success', 'host': serializer.data})
            else:
                return JsonResponse({'status': 'error', 'errors': serializer.errors})
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Host not found'})

    elif request.method == 'DELETE':
        # 删除（逻辑删除）主机记录
        try:
            host = HostsInfo.objects.get(id=host_id)
            host.is_deleted = True
            host.save()
            serializer = HostsInfoSerializer(host)
            return JsonResponse({'status': 'success', 'host': serializer.data})
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Host not found'})

    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

# @api_view(['GET', 'POST', 'DELETE'])
# def hostinfo_detail(request, pk):
#     """
#         指标：
#         判断是否存在返回404
#         get请求返回监控对象信息
#         post请求更新信息，失败返回400
#         删除数据，返回204
#     """
#     try:
#         hostinfo = HostsInfo.objects.get(id=pk)
#     except Metrics.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = HostsInfoSerializer(hostinfo)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = HostsInfoSerializer(hostinfo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         hostinfo.is_deleted = True
#         hostinfo.save()
#         return Response(status=status.HTTP_204_NO_CONTENT)
