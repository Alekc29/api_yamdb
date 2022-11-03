from django.contrib.auth.models import AbstractUser
from django.db import models

CHOICES = ('admin', 'moderator', 'user',)


class User(AbstractUser):
    username = models.CharField(
        'Ник',
        max_length=150,
        unique=True,
    )
    email = models.EmailField(
        'эл. почта',
        unique=True
    )
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
    role = models.CharField(
        'Статус',
        max_length=10,
        #choices=CHOICES,
        default='user',
    )
    
    def __str__(self):
        return self.username