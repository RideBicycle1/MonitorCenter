from rest_framework import serializers
from .models import MonitorObject, Metrics


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
