from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework_extensions.mixins import DetailSerializerMixin

from apps.sensor_portal.models import Sensor
from apps.sensor_portal.serializers.sensors import (SensorSerializer,GetSensorSerializer,PostSensorSerializer,PatchSensorSerializer,PutSensorSerializer,ListSensorSerializer)
from utils.mixin import StandardResultsSetPagination


class SensorsViewSet(DetailSerializerMixin, viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    max_paginate_by = 100
    serializer_class = SensorSerializer
    pagination_class = StandardResultsSetPagination
    # permission_classes = (IsAuthenticated,)
    #
    # def get_queryset(self):
    #     return Teacher.objects
    # @extend_schema(
    #     request=TeacherSerializer,
    #     responses={201: TeacherSerializer,
    #                200: TeacherSerializer},
    # )
    def create(self, request):
        # your non-standard behaviour
        return super().create(request)

    def get_serializer_class(self):
        if self.action == 'list':
            return ListSensorSerializer
        elif self.action == 'retrieve':
            return GetSensorSerializer
        elif self.action == 'create':
            return PostSensorSerializer
        elif self.action == 'update':
            return PutSensorSerializer
        elif self.action == 'partial_update':
            return PatchSensorSerializer
        # elif self.action == 'destroy':
        #     return TeacherSerializer
        else:
            return SensorSerializer


#
# `    def create(self, request):
#         # your non-standard behaviour
#         return super().create(request)