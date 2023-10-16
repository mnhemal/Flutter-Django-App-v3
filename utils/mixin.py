from django.db import models
from django.utils.translation import gettext_lazy as _
from drf_spectacular.contrib.rest_framework_simplejwt import SimpleJWTScheme
from rest_framework import HTTP_HEADER_ENCODING
from typing import Set


class TimeStampModelMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseModelMixin(TimeStampModelMixin):
    class Meta:
        abstract = True


from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 600
    page_size_query_param = 'page_size'
    max_page_size = 100