from rest_framework import serializers
from users.models import User


class SignUpSerializer(serializers.ModelSerializer):

    def validate_username_not_me(self, username):
        if username == 'me':
            raise serializers.ValidationError(
                ('Ник не может быть <me>.'),
                params={'user': username},
            )
        return username

    def validate_unique_username_and_email(self, username, email):
        if User.objects.count(username=username):
            raise serializers.ValidationError(
                ('К сожалению такой ник уже есть в базе.'),
                params={'username': username},
            )
        if User.objects.count(email=email):
            raise serializers.ValidationError(
                ('К сожалению email уже использовался для регистрации.'),
                params={'email': email},
            )
        return username, email

    class Meta:
        fields = ('username',
                  'email',)
        model = User


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
