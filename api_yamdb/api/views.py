from rest_framework import viewsets
# from rest_framework.permissions import IsAdminOrReadOnly

from titles.models import Category, Genre #, Comment, Genre, Review, Title
from .serializers import CategorySerializer, GenreSerializer


class CategoryGenreViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAdminOrReadOnly,)
    search_fields = ('name',) 

class CategoryViewSet(CategoryGenreViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GenreViewSet(CategoryGenreViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
