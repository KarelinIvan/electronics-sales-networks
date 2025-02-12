from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """ Пользователи сети """
    username = models.CharField(max_length=25, verbose_name='Имя пользователя')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Телефон', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)
    company = models.CharField(
        max_length=255, verbose_name='Компания', **NULLABLE)
    position = models.CharField(
        max_length=100, verbose_name='Должность', **NULLABLE)
    level = models.PositiveSmallIntegerField(
        choices=((0, 'Завод'), (1, 'Розничная сеть'),
                 (2, 'Индивидуальный предприниматель')),
        verbose_name='Уровень доступа',
        default=0
    )
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    is_staff = models.BooleanField(
        default=False, verbose_name='Статус сотрудника')
    date_joined = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата регистрации')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
