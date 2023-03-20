from django.shortcuts import render
from rest_framework.utils import json

# Create your views here.
from MonitorCenter import models
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .models import MonitorObject, Metrics
from .serializers import MonitorObjectSerializer, MetricsSerializer


@api_view(['GET', 'POST'])
def monitor_object_list(request):
    """
        查询全部监控对象，或者新增一个监控对象
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
        查询全部监控指标，或者新增一个监控指标
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


@api_view(['GET', 'POST', 'DELETE'])
def monitor_object_detail(request, pk):
    """
        查询/更新一个监控对象，或者删除一个监控对象
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
        查询/更新一个监控指标，或者删除一个监控指标
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


def index(request):
    """
    监控对象视图
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