from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework.permissions import IsAdminOrReadOnly

from users.models import User
# from .permissions import IsAdminOnlyPermission
from titles.models import Category, Genre, Title #, Comment, Review
from .serializers import CategorySerializer, GenreSerializer, TitleSerializer, UserSerializer


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


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save()

    
