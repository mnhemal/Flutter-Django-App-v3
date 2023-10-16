from rest_framework import serializers

from apps.user_portal.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password_hash', 'first_name', 'last_name')
        exclude = ('created_at', 'updated_at')

class PostUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password_hash', 'first_name', 'last_name')

class PutUserSerializer(GetUserSerializer):
    pass

class PatchUserSerializer(GetUserSerializer):
    pass

class ListUserSerializer(GetUserSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password_hash', 'first_name', 'last_name')