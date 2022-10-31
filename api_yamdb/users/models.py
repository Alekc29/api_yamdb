from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(
        'Имя',
        max_length=150,
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=150,
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.SlugField(
        default='user',
        unique=True,
    )