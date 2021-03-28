from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

from django.conf import settings


class User(AbstractUser):
    ROLE_USER = 'user'
    ROLE_MODERATOR = 'moderator'
    ROLE_ADMIN = 'admin'
    USERS_ROLE = (
        (ROLE_USER, 'Пользователь'),
        (ROLE_MODERATOR, 'Модератор'),
        (ROLE_ADMIN, 'Админ'),
    )
    email = models.EmailField('e-mail', unique=True)
    bio = models.TextField(
        max_length=500,
        blank=True,
        null=True,
    )
    role = models.CharField(
        verbose_name='Роль пользователя',
        max_length=10,
        choices=USERS_ROLE,
        default=ROLE_USER,
    )
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'
    def __str__(self):
        return self.email


class ConfirmationCode(models.Model):
    confirmation_code = models.CharField(max_length=32)
    email = models.EmailField(max_length=254, unique=True)
    code_date = models.DateTimeField(auto_now_add=True)
