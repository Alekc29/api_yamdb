from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from users.models import User
from .serializers import UserSerializer
from .permissions import IsAdminOnlyPermission

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save()

    