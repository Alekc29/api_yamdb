from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import validate_username

ENUM = [('admin', 'admin'),
        ('moderator', 'moderator'),
        ('user', 'user')]


class User(AbstractUser):
    username = models.CharField(
        'Ник',
        validators=(validate_username,),
        max_length=150,
        unique=True,
        blank=False,
        null=False,
    )
    email = models.EmailField(
        'эл. почта',
        unique=True,
        blank=False,
        null=False,
    )
    first_name = models.CharField(
        'Имя',
        max_length=150,
        blank=True,
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=150,
        blank=True,
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        'Статус',
        max_length=10,
        choices=ENUM,
        default='user',
        blank=True,
    )
    confirmation_code = models.CharField(
        'код подтверждения',
        max_length=255,
        null=True,
        blank=False,
        default='XXXX'
    )

    
    @property
    def is_user(self):
        return self.role == 'user'
    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_moderator(self):
        return self.role == 'moderator'

    def __str__(self):
        return self.username