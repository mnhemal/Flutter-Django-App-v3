from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework_extensions.mixins import DetailSerializerMixin

from apps.user_portal.models import User
from apps.user_portal.serializers.users import(UserSerializer, GetUserSerializer, PostUserSerializer,PutUserSerializer, PatchUserSerializer, ListUserSerializer)
from utils.mixin import StandardResultsSetPagination


class UsersViewSet(DetailSerializerMixin, viewsets.ModelViewSet):
    queryset = User.objects.all()
    max_paginate_by = 100
    serializer_class = UserSerializer
    pagination_class = StandardResultsSetPagination
    # permission_classes = (IsAuthenticated,)
    #
    # def get_queryset(self):
    #     return Student.objects
    # @extend_schema(
    #     request=StudentSerializer,
    #     responses={201: StudentSerializer,
    #                200: StudentSerializer},
    # )
    def create(self, request):
        # your non-standard behaviour
        return super().create(request)

    def get_serializer_class(self):
        if self.action == 'list':
            return ListUserSerializer
        elif self.action == 'retrieve':
            return GetUserSerializer
        elif self.action == 'create':
            return PostUserSerializer
        elif self.action == 'update':
            return PutUserSerializer
        elif self.action == 'partial_update':
            return PatchUserSerializer
        # elif self.action == 'destroy':
        #     return StudentSerializer
        else:
            return UserSerializer


#
# `    def create(self, request):
#         # your non-standard behaviour
#         return super().create(request)