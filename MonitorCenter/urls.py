from django.urls import path

from . import views

app_name = 'MonitorCenter'

urlpatterns = [
    path('', views.index, name='index'),
    path('sys/', views.sysindex, name='sysindex'),
 ]