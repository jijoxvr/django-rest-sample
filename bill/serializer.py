from rest_framework import serializers
from .models import Bill

class BillModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill


class BillSerializer(serializers.Serializer):
    vendor = serializers.PrimaryKeyRelatedField()
    amount = serializers.FloatField()
    bill_date = serializers.DateField()
    due_date = serializers.DateField()
