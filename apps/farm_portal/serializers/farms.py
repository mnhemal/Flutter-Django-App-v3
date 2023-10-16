from rest_framework import serializers

from apps.farm_portal.models import Farm


class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = '__all__'

class GetFarmSerializer(serializers.ModelSerializer):
    """
    Farm Serializer
    """
    class Meta:
        model = Farm
        exclude = ('created_at', 'updated_at')

class PostFarmSerializer(GetFarmSerializer):
 pass

class PutFarmSerializer(GetFarmSerializer):
 pass

class PatchFarmSerializer(GetFarmSerializer):
 pass

class ListFarmSerializer(GetFarmSerializer):
    """
    Farm Serializer for listing selected data.
    """
    class Meta:
        model = Farm
        fields = ('id', 'farm_name', 'location')


