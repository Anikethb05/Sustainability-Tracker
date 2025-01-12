from django.shortcuts import render
from rest_framework import viewsets
from .models import SustainabilityAction
from .serializers import SustainabilityActionSerializer
import json
from django.conf import settings
import os

class SustainabilityActionViewSet(viewsets.ModelViewSet):
    queryset = SustainabilityAction.objects.all()
    serializer_class = SustainabilityActionSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        self._save_to_json()
        return instance

    def perform_update(self, serializer):
        instance = serializer.save()
        self._save_to_json()
        return instance

    def perform_destroy(self, instance):
        instance.delete()
        self._save_to_json()

    def _save_to_json(self):
        """Save all actions to a JSON file"""
        actions = self.get_queryset()
        serializer = self.get_serializer(actions, many=True)
        json_file_path = os.path.join(settings.BASE_DIR, 'actions_backup.json')
        
        with open(json_file_path, 'w') as f:
            json.dump(serializer.data, f, indent=2)
