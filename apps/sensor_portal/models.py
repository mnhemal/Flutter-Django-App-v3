from django.db import models

from apps.farm_portal.models import Farm
from utils.mixin import BaseModelMixin


class Sensor(BaseModelMixin):
    """
    Sensor Data Database Schema
    """
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    soil_moisture = models.FloatField()
    light_intensity = models.FloatField()
    rainfall = models.FloatField()
    wind_speed = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ID: {self.id}, Farm: {self.farm.farm_name}, Temperature: {self.temperature}, Humidity: {self.humidity}"
