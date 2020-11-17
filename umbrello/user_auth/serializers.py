from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    EmailField,
    ValidationError
)

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
        print(validated_data)
        user = User(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user = user)
        return token

    def validate(self, data):
        if not User.objects.filter(username = data.get("username")).filter(email = data.get("email")).exists():
            return data
        raise ValidationError('user already exist')