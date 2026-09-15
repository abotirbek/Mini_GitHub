from rest_framework import serializers
from accounts.models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'phone',
            'email',
            'avatar',
            'password',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)