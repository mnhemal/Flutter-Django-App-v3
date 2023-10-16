from django.urls import include, path

from .views import *
from rest_framework.routers import DefaultRouter

from .views.farms import FarmsViewSet

app_name = "farm_portal"
router = DefaultRouter()
router.register(r"farms", FarmsViewSet, basename="farms")
urlpatterns = [
    path("", include(router.urls)),
    # path("students/", StudentsViewSet.as_view(), name="students"),
]