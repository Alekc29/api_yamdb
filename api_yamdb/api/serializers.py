from rest_framework import serializers

from users.models import User

class UserSerializer(serializers.ModelSerializer):
    

    def validate_username(self, username):
        if username == 'me':
            raise serializers.ValidationError('Использовать "me" нельзя.')
        return username

    class Meta:
        fields = ('username',
                  'email',
                  'first_name',
                  'last_name',
                  'bio',
                  'role')
        model = User