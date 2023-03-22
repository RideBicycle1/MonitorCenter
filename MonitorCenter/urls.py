from django.urls import path, re_path

from MonitorCenter import views

app_name = 'MonitorCenter'

urlpatterns = [
    # 对象接口路径
    path('objects/', views.MonitorObjectview.index, name='index'),
    re_path(r'^objects/api/$', views.MonitorObjectview.monitor_object_list),
    re_path(r'^objects/api/(?P<pk>[0-9]+)$', views.MonitorObjectview.monitor_object_detail),
    # 指标接口路径
    path('metrics/', views.metricsview.metric, name='metric'),
    re_path(r'^sysmetrics/api/$', views.metricsview.get_sys_metrics),
    re_path(r'^metrics/api/$', views.metricsview.metrics_list),
    re_path(r'^metrics/api/(?P<pk>[0-9]+)$', views.metricsview.metrics_detail),
    # 系统信息接口路径
    re_path(r'^add_sysmetrics/api/$', views.metricsview.add_sys_metrics),
    path('sys/', views.sysinfoview.sysindex, name='sysindex'),
    re_path(r'^sysinfo/api/$', views.sysinfoview.sysinfo_object_list),
    re_path(r'^sysinfo/api/(?P<pk>[0-9]+)$', views.sysinfoview.sysinfo_object_detail),
    # 主机信息接口路径
    re_path(r'^hostinfo/api/$', views.hostinfoview.host_object_list),
    re_path(r'^hostinfo/api/(?P<pk>[0-9]+)$', views.hostinfoview.hostinfo_detail),
 ]
