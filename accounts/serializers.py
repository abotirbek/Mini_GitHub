from django.core.validators import MaxLengthValidator
from rest_framework import serializers
from accounts.models import CustomUser
import re


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

    def validate_username(self, username):
        pattern = r"^[a-zA-Z0-9_-]{3,16}$"
        if re.match(pattern, username):
            return username
        raise serializers.ValidationError('Username requirements: a-z, A-Z, 0-9, _, length 3-16')

    def validate_email(self, email):
        return email.lower()

    def validate_phone(self, phone):
        pattern = r"^[0-9]{9}$"
        if phone[:4] != '+998':
            raise serializers.ValidationError('Phone number should start with +998')
        if not re.match(pattern, phone[4:]):
            raise serializers.ValidationError('Phone number should consist of numbers')
        return phone

    def validate_password(self, password):
        pattern = r"^[a-zA-Z0-9]{8,20}$"
        if re.match(pattern, password):
            return password
        raise serializers.ValidationError("Password requirements: a-z, A-Z, 0-9, length 8-20")



class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField(min_length=8, validators=[MaxLengthValidator(20)])

    def validate_old_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError('Old password is incorrect.')
        return value

    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user
