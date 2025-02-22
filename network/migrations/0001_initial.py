# Generated by Django 5.1.2 on 2025-02-17 18:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название', max_length=255, verbose_name='название')),
                ('email', models.EmailField(help_text='Введите электронную почту', max_length=254, unique=True, verbose_name='электронная почта')),
                ('country', models.CharField(help_text='Введите страну', max_length=255, verbose_name='страна')),
                ('city', models.CharField(help_text='Введите город', max_length=255, verbose_name='город')),
                ('street', models.CharField(help_text='Введите улицу', max_length=255, verbose_name='улица')),
                ('house_number', models.CharField(help_text='Введите номер дома', max_length=150, verbose_name='дом')),
                ('level', models.PositiveSmallIntegerField(choices=[(0, 'завод'), (1, 'розничная сеть'), (2, 'индивидуальный предприниматель')], help_text='Выберите уровень', verbose_name='уровень в сети')),
                ('debt', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='задолженность перед поставщиком')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='создан')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suppliers', to='network.supplier', verbose_name='поставщик')),
            ],
            options={
                'verbose_name': 'поставщик',
                'verbose_name_plural': 'поставщики',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(help_text='Введите название продукта', max_length=255, verbose_name='название продукта')),
                ('model', models.CharField(help_text='Введите модель', max_length=255, verbose_name='модель')),
                ('release_date', models.DateField(help_text='Введите дату выхода продукта на рынок', verbose_name='дата выхода продукта на рынок')),
                ('supplier', models.ForeignKey(help_text='Выберите поставщика', on_delete=django.db.models.deletion.CASCADE, to='network.supplier', verbose_name='поставщик')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
    ]
