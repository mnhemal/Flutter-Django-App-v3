from django.urls import include, path

from .views import *
from rest_framework.routers import DefaultRouter

from .views.sensors import SensorsViewSet

app_name = "sensor_portal"
router = DefaultRouter()
router.register(r"sensors", SensorsViewSet, basename="sensors")
urlpatterns = [
    path("", include(router.urls)),
    # path("students/", StudentsViewSet.as_view(), name="students"),
]