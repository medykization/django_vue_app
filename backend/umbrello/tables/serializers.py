from tables.models import Board
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, ValidationError


class BoardSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = ['name', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    '''
    def create(self, validated_data):
        board = Board(
            owner_id=validated_data['user'], name=validated_data['name'])
        board.save()

    def validate(self, data):
        user = self.user
        if not Board.objects.filter(owner_id=user).filter(name=data.get("name")).exists():
            data['user'] = user
            return data
        raise ValidationError('board already exist')
    '''
