from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from django.contrib.auth import authenticate

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class UserLoginSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=64)
    user_pw = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        user_id = data.get("user_id", None)
        user_pw = data.get("user_pw", None)
        print("serializer-data: ", user_id, ", ", user_pw)
        user = authenticate(user_id=user_id, user_pw=user_pw)

        print("##### step 1: ", user)
        if user is None:
            return {
                'user_id': 'None'
            }
        print("##### step 2")
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            print("jwt_token: ", jwt_token)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'user_id': user.user_id,
            'token': jwt_token
        }