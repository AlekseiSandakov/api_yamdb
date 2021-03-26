from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

from django.conf import settings


class User(AbstractUser):
    first_name = models.TextField(max_length=500, blank=True)
    last_name = models.TextField(max_length=500, blank=True)
    username = models.TextField(max_length=500, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    role = models.DateField(null=True, blank=True)
    confirmation_code = models.CharField(
        max_length=36,
        blank=True,
        null=True,
        unique=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    USER_ROLES = [
        ('admin', 'Администратор'),
        ('moderator', 'Модератор'),
        ('user', 'Пользователь')
    ]

    @property
    def is_admin(self):
        return self.role == 'admin' or self.is_staff

    @property
    def is_moderator(self):
        return self.role == 'moderator'

    class Meta:
        ordering = ('id', )
