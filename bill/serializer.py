from rest_framework import serializers
from .models import Bill
from vendor.models import Vendor

class BillModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bill
        fields = '__all__'


# class BillSerializer(serializers.Serializer):
#     vendor = serializers.PrimaryKeyRelatedField()
#     amount = serializers.FloatField()
#     bill_date = serializers.DateField()
#     due_date = serializers.DateField()
