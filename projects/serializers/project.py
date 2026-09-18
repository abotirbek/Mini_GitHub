from rest_framework import serializers
from task_manager.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'name',
            'description',
            'owner',
            'visibility',
            'members',
        ]