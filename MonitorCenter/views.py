

from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404

from MonitorCenter import models


def index(request):
    """
    监控对象视图
    :param request:
    :return:
    """
    MonitorObject = models.MonitorObject.objects.all()
    return render(request, 'MonitorCenter/index.html', locals())