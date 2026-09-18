from rest_framework import serializers
from task_manager.models import ProjectMember



class ProjectMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMember
        fields = [
            'projects',
            'user',
        ]
