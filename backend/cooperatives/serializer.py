from .models import Cooperative
from rest_framework import serializers


class CooperativeSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    
    class Meta:
        model = Cooperative
        fields = ('name',
                  'short_description',
                  'description',
                  'logo',
                  'phone',
                  'facebook_profile',
                  'address',
                  'map_latitude',
                  'map_longitude',
                  'whatsapp',
                  'category')

