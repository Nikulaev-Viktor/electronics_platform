from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=50, verbose_name='Имя', help_text='Введите имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия', help_text='Введите фамилию', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='Электронная почта',
                              help_text='Введите электронную почту')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона',
                                    help_text='Введите номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/avatars/', verbose_name='аватар', **NULLABLE,
                               help_text='загрузите свой аватар')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.first_name} {self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
