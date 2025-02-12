from django.db import models


class NetworkElement(models.Model):
    """ Модель элементов сети"""
    LEVEL_CHOICES = (
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    )

    NULLABLE = {'blank': True, 'null': True}

    name = models.CharField(max_length=255, verbose_name='Наименование')
    email = models.EmailField(verbose_name='Email')
    country = models.CharField(
        max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=255, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL,
                                 **NULLABLE, related_name='customers', verbose_name='Поставщик')
    debt_to_supplier = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name='Задолженность перед поставщиком')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Элемент сети'
        verbose_name_plural = 'Элементы сети'

    def __str__(self):
        return self.name


class Product(models.Model):
    """ Модель продукта"""
    element = models.ForeignKey(
        NetworkElement, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255, verbose_name='Наименование продукта')
    model = models.CharField(max_length=50, verbose_name='Модель')
    release_date = models.DateField(
        verbose_name='Дата выхода продукта на рынок')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


def __str__(self):
    return f'{self.element.name}: {self.name}'
