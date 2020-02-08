from rest_framework import serializers
from .models import ForgotPasswordToken


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ForgotPasswordConfirmSerializer(serializers.ModelSerializer):
    new_password1 = serializers.CharField(max_length=100)
    new_password2 = serializers.CharField(max_length=100)

    class Meta:
        model = ForgotPasswordToken
        fields = ['new_password1', 'new_password2', 'uid', 'token']

    def validate(self, data):
        if data['new_password1'] != data['new_password2']:
            raise serializers.ValidationError('passwords don\'t match!')
        return data


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(style={'input_type': 'password'})
    new_password = serializers.CharField(style={'input_type': 'password'})
    repeat_new_password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):
        if data['new_password'] != data['repeat_new_password']:
            raise serializers.ValidationError('passwords don\'t match!')
        return data
