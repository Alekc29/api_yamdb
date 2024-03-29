from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User

from .serializers import GetTokenSerializer, SignUpSerializer


def send_email(data):
    email = EmailMessage(
        subject='Код подтверждения для доступа к API:',
        body=f'{data.confirmation_code}',
        to=[data.email, ]
    )
    email.send()


@api_view(['POST', ])
def post_signup(request):
    """
    Получить код подтверждения на переданный email.
    Права доступа: Доступно без токена.
    Использовать имя 'me' в качестве username запрещено.
    Поля email и username должны быть уникальными.
    """
    serializer = SignUpSerializer(data=request.data)
    if (
        not isinstance(request.data, dict)
        or request.data.get('username') is None
        or request.data.get('email') is None
    ):
        serializer.is_valid()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    username = request.data['username']
    email = request.data['email']
    obj = User.objects.filter(username=username, email=email).first()
    if obj is not None:
        send_email(obj)
        return Response('Повторная отправка кода.', status=status.HTTP_200_OK)
    if serializer.is_valid():
        data = serializer.save()
        data.confirmation_code = default_token_generator.make_token(data)
        data = serializer.save()
        send_email(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
def post_get_token(request):
    """
    Получение JWT-токена в обмен на Ник и код подтверждения.
    Права доступа: Доступно без токена.
    """
    serializer = GetTokenSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        user = get_object_or_404(
            User,
            username=data['username']
        )
        if data.get('confirmation_code') == user.confirmation_code:
            token = RefreshToken.for_user(user).access_token
            serializer.save
            return Response(
                {'token': str(token)},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {'confirmation_code': 'Неверный код подтверждения!'},
            status=status.HTTP_400_BAD_REQUEST
        )
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )
