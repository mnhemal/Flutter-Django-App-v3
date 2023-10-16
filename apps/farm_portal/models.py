from django.db import models

from apps.user_portal.models import User
from utils.mixin import BaseModelMixin


class Farm(BaseModelMixin):
    """
    Farm Database Schema
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    farm_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    size_acres = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ID: {self.id}, Farm Name: {self.farm_name}, Location: {self.location}"