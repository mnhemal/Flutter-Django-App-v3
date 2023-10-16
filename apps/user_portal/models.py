from django.db import models

from utils.mixin import BaseModelMixin


# Create your models here.

class User(BaseModelMixin):
    """
    User Database Schema
    """
    username = models.CharField(max_length=255)
    password_hash = models.CharField(max_length=255)
    email = models.EmailField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ID: {self.id}, Username: {self.username}, Email: {self.email}"