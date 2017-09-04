from rest_framework import serializers
from .models import Vendor

class VendorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class VendorSerializer(serializers.Serializer):
    name = serializers.CharField()
    service_type = serializers.CharField(required=False)
    since = serializers.DateField(required=False)
    currency = serializers.CharField(required=False)
    is_active = serializers.BooleanField(required=False)
