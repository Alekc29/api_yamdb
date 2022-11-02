from rest_framework import viewsets

from titles.models import Category, Genre #, Comment, Genre, Review, Title
from .serializers import CategorySerializer, GenreSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = (IsAdminOrReadOnly,)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    # permission_classes = (IsAdminOrReadOnly,)