from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User=get_user_model()


class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=255)
    password=serializers.CharField(max_length=128,style={'input_type': 'password'},required=True)

    class Meta:
        model = User
        fields = ['username', 'password',]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)
        if username is None:
            raise serializers.ValidationError(
                'Provide username to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'

        user = authenticate(username=username, password=password)
        if user:
                if user.is_active:
                    data["user"]=user
                else:
                    raise serializers.ValidationError(
                        'Deactivated User.'
                    )

        else:
                raise serializers.ValidationError(
                    'Unable to login with given credentials.'
                )
        return data
