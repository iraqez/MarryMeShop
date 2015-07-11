# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'Товары', 'verbose_name': 'Товар'},
        ),
        migrations.AlterField(
            model_name='category',
            name='first_menu',
            field=models.CharField(max_length=30, verbose_name='Верхний уровень меню', choices=[('a', 'Для невесты'), ('b', 'Для жениха'), ('c', 'Для автомобиля'), ('d', 'Для детей'), ('e', 'Аксессуары')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=50, verbose_name='Производитель'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создано'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активно'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_bestseller',
            field=models.BooleanField(default=False, verbose_name='Бестселлер'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_featured',
            field=models.BooleanField(default=False, verbose_name='Распродажа'),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_description',
            field=models.CharField(max_length=255, help_text='Дескрипторы метатегов', verbose_name='Дескрипторы'),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_keywords',
            field=models.CharField(max_length=255, help_text='Добавляет ключевые слова в мета-теги странички для СЕО поиска.', verbose_name='Ключевые слова'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.DecimalField(max_digits=9, default=0.0, blank=True, decimal_places=2, verbose_name='Старая цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(max_length=50, verbose_name='СКЮ'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(help_text='Уникальное значение в адресной строки для товара, добавляется автоматически.', max_length=255, unique=True, verbose_name='Адресная строка'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Изменено'),
        ),
    ]
