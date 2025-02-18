from django.core.exceptions import ValidationError
from django.db import models

from users.models import NULLABLE


class Supplier(models.Model):
    LEVEL_CHOICES = (
        (0, 'завод'),
        (1, 'розничная сеть'),
        (2, 'индивидуальный предприниматель')
    )

    name = models.CharField(max_length=255, verbose_name='название', help_text='Введите название')
    email = models.EmailField(unique=True, verbose_name='электронная почта',
                              help_text='Введите электронную почту')
    country = models.CharField(max_length=255, verbose_name='страна', help_text='Введите страну')
    city = models.CharField(max_length=255, verbose_name='город', help_text='Введите город')
    street = models.CharField(max_length=255, verbose_name='улица', help_text='Введите улицу')
    house_number = models.CharField(max_length=150, verbose_name='дом', help_text='Введите номер дома')
    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES, verbose_name='уровень в сети',
                                             help_text='Выберите уровень')
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='поставщик', related_name='suppliers',
                                 **NULLABLE, help_text='Выберите поставщика')
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00,
                               verbose_name='задолженность перед поставщиком')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создан')

    def clean(self):
        if self.level == 0 and self.debt:
            raise ValidationError('Завод не может иметь задолженность перед поставщиком')
        if self.level == 0 and self.supplier:
            raise ValidationError('Завод не должен иметь поставщика')

    def __str__(self):
        return f'{self.name} ({self.country})'

    class Meta:
        verbose_name = 'звено сети'
        verbose_name_plural = 'звенья сети'


class Product(models.Model):
    product_name = models.CharField(max_length=255, verbose_name='название продукта',
                                    help_text='Введите название продукта')
    model = models.CharField(max_length=255, verbose_name='модель', help_text='Введите модель')
    release_date = models.DateField(verbose_name='дата выхода продукта на рынок',
                                    help_text='Введите дату выхода продукта на рынок')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='поставщик',
                                 help_text='Выберите поставщика', related_name='products')

    def __str__(self):
        return f'{self.product_name} - {self.model}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
