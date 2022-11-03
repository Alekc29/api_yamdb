from rest_framework import serializers

from titles.models import Category, Genre, Title # Comment,  Review, 

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