from rest_framework import serializers

from apps.sensor_portal.models import Sensor


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'

class GetSensorSerializer(serializers.ModelSerializer):
    """
    Sensor Serializer
    """
    class Meta:
        model = Sensor
        exclude = ('created_at',)

class PostSensorSerializer(GetSensorSerializer):
 pass

class PutSensorSerializer(GetSensorSerializer):
    """
    Sensor Serializer for full update.
    """
    pass

class PatchSensorSerializer(GetSensorSerializer):
    """
    Sensor Serializer for partial update.
    """
    pass

class ListSensorSerializer(GetSensorSerializer):
    """
    Sensor Serializer for listing selected data.
    """
    class Meta:
        model = Sensor
        fields = ('id', 'temperature', 'humidity')
