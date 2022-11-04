from rest_framework import serializers

from titles.models import Category, Genre, Title # Comment,  Review, 
from users.models import User


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ("name", "slug")


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ("name", "slug")


class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Title
        fields = ("name", "year", "rating", "description", "genre", "category")
from rest_framework import serializers


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
