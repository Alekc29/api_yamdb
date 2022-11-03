from rest_framework import viewsets
# from rest_framework.permissions import IsAdminOrReadOnly

from titles.models import Category, Genre, Title #, Comment, Review
from .serializers import CategorySerializer, GenreSerializer, TitleSerializer


class CategoryGenreViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAdminOrReadOnly,)
    search_fields = ('name',) 

class CategoryViewSet(CategoryGenreViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GenreViewSet(CategoryGenreViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer