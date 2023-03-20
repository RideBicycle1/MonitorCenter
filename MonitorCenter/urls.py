from django.urls import path, re_path
from . import views

app_name = 'MonitorCenter'

urlpatterns = [
    path('user/login', views.login),
    path('user/info', views.info),
    path('objects/', views.index, name='index'),
    re_path(r'^objects/api/$', views.monitor_object_list),
    re_path(r'^objects/api/(?P<pk>[0-9]+)$', views.monitor_object_detail),
    path('metrics/', views.metric, name='metric'),
    re_path(r'^sysmetrics/api/$', views.get_sys_metrics),
    re_path(r'^add_sysmetrics/api/$', views.add_sys_metrics),
    re_path(r'^metrics/api/$', views.metrics_list),
    re_path(r'^metrics/api/(?P<pk>[0-9]+)$', views.metrics_detail),
    path('sys/', views.sysindex, name='sysindex'),
    re_path(r'^sysinfo/api/$', views.sysinfo_object_list),
    re_path(r'^sysinfo/api/(?P<pk>[0-9]+)$', views.sysinfo_object_detail),
 ]
