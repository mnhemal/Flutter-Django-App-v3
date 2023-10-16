from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework_extensions.mixins import DetailSerializerMixin

from apps.farm_portal.models import Farm
from apps.farm_portal.serializers.farms import (FarmSerializer,GetFarmSerializer,PostFarmSerializer,PatchFarmSerializer,PutFarmSerializer,ListFarmSerializer)
from utils.mixin import StandardResultsSetPagination


class FarmsViewSet(DetailSerializerMixin, viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    max_paginate_by = 100
    serializer_class = FarmSerializer
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
            return ListFarmSerializer
        elif self.action == 'retrieve':
            return GetFarmSerializer
        elif self.action == 'create':
            return PostFarmSerializer
        elif self.action == 'update':
            return PutFarmSerializer
        elif self.action == 'partial_update':
            return PatchFarmSerializer
        # elif self.action == 'destroy':
        #     return TeacherSerializer
        else:
            return FarmSerializer


#
# `    def create(self, request):
#         # your non-standard behaviour
#         return super().create(request)