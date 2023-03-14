from django.urls import path, re_path

from . import views

app_name = 'MonitorCenter'

urlpatterns = [
    path('objects/', views.index, name='index'),
    re_path(r'^objects/$', views.monitor_object_list),
    re_path(r'^objects/(?P<pk>[0-9]+)$', views.monitor_object_detail),
    path('metrics/', views.metric, name='metric'),
    re_path(r'^metrics/$', views.metrics_list),
    re_path(r'^metrics/(?P<pk>[0-9]+)$', views.metrics_detail),
    path('sys/', views.sysindex, name='sysindex'),
 ]
