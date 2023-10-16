from django.urls import include, path

from .views import *
from rest_framework.routers import DefaultRouter

from .views.users import UsersViewSet

app_name = "user_portal"
router = DefaultRouter()
router.register(r"users", UsersViewSet, basename="users")
urlpatterns = [
    path("", include(router.urls)),
    # path("students/", StudentsViewSet.as_view(), name="students"),
]