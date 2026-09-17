from rest_framework import serializers
from task_manager.models import Project, ProjectMember


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


class ProjectMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMember
        fields = [
            'project',
            'user',
        ]
