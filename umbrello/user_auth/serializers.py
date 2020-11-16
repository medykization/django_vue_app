from django.contrib.auth.models import User
from rest_framework.serializers import (
    ModelSerializer,
    CharField
)

class UserSerializer(ModelSerializer):
    username = CharField()
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            ]
        extra_kwargs = {"password":
                        {"write_only": True}
                        }

    def validate(self, data):
        return data