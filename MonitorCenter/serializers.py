from rest_framework import serializers
from MonitorCenter.models import MonitorObject, Metrics, SysInfoManage, HostsInfo


class MonitorObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitorObject
        fields = '__all__'
        read_only_fields = ('id', 'create_time')


class MetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metrics
        fields = '__all__'
        read_only_fields = ('id', 'create_time')


class SysInfoManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysInfoManage
        fields = '__all__'
        read_only_fields = ('id', 'create_time')


class HostsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostsInfo
        fields = '__all__'
        read_only_fields = ('id', 'create_time')
