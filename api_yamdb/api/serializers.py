from django.core.exceptions import ValidationError
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from reviews.models import Category, Comment, Genre, Review, Title
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
    genre = GenreSerializer(many=True)
    category = CategorySerializer()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Title
        fields = (
            'id', 'name', 'year', 'rating', 'description', 'genre', 'category'
        )

    def get_rating(self, obj):
        return obj.reviews.aggregate(Avg('score')).get('score__avg')


class TitleForAdminSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        many=True,
        slug_field='slug',
        queryset=Genre.objects.all()
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug'
    )

    class Meta:
        model = Title
        fields = (
            'id', 'name', 'year', 'rating', 'description', 'genre', 'category'
        )


class ReviewSerializer(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    def validate_score(self, score):
        if 0 > score > 10:
            raise serializers.ValidationError('Оцените от 1 до 10')
        return score

    def validate(self, data):
        request = self.context['request']
        author = request.user
        title_id = self.context.get('view').kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)
        if request.method == 'POST' and Review.objects.filter(
                title=title, author=author).exists():
            raise ValidationError('Вы уже оставили отзыв')
        return data

    class Meta:
        model = Review
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    review = serializers.SlugRelatedField(
        slug_field='text',
        read_only=True
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('username',
                  'email',
                  'first_name',
                  'last_name',
                  'bio',
                  'role')
        model = User


class NotAdminSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('username',
                  'email',
                  'first_name',
                  'last_name',
                  'bio',
                  'role')
        read_only_fields = ('role',)
        model = User


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
