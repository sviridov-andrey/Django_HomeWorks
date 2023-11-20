import random
from django.contrib.auth.models import AbstractUser
from django.db import models
from catalog.utils import NULLABLE


default_code = ''.join([str(random.randint(0, 9)) for _ in range(12)])


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='страна', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='активность')
    email_verified = models.BooleanField(default=False, verbose_name='верификация почты')
    ver_code = models.CharField(max_length=15, default=default_code, verbose_name='код из письма')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f' {self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
