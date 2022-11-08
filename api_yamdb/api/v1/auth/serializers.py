from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from users.models import User


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('username',
                  'email',)
        model = User
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=('username', 'email')
            )
        ]

    def validate_username(self, username):
        if username == 'me':
            raise serializers.ValidationError(
                ('Ник не может быть <me>.'),
                params={'username': username},
            )
        return username


class GetTokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        label='Ник',
        required=True
    )
    confirmation_code = serializers.CharField(
        label='Код подтверждения',
        required=True
    )

    class Meta:
        fields = ('username',
                  'confirmation_code')
        model = User
