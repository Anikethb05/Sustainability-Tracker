from rest_framework import serializers
from .models import SustainabilityAction

class SustainabilityActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SustainabilityAction
        fields = ['id', 'action', 'date', 'points', 'created_at']
        read_only_fields = ['created_at']