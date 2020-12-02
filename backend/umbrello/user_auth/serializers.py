from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from django.utils.text import gettext_lazy
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    EmailField,
    ValidationError
)

##TODO update this class
class UserSerializer(ModelSerializer):
    username = CharField()
    email = EmailField()
    password = CharField(
        write_only=True,
        required=True,
    )
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            ]

    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()

    def validate(self, data):
        if not User.objects.filter(username = data.get("username")).filter(email = data.get("email")).exists():
            return data
        raise ValidationError('user already exist')

class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': gettext_lazy('Token is invalid or expired')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')