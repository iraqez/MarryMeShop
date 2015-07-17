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
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары', 'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='category',
            name='first_menu',
            field=models.CharField(
                choices=[('neveste', 'Для невесты'), ('zhenihu', 'Для жениха'), ('auto', 'Для автомобиля'),
                         ('detyam', 'Для детей'), ('acsessories', 'Аксессуары')], verbose_name='Верхний уровень меню',
                max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(verbose_name='Производитель', max_length=50),
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
            field=models.BooleanField(verbose_name='Активно', default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_bestseller',
            field=models.BooleanField(verbose_name='Бестселлер', default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_featured',
            field=models.BooleanField(verbose_name='Распродажа', default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_description',
            field=models.CharField(verbose_name='Дескрипторы', max_length=255, help_text='Дескрипторы метатегов'),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_keywords',
            field=models.CharField(verbose_name='Ключевые слова', max_length=255,
                                   help_text='Добавляет ключевые слова в мета-теги странички для СЕО поиска.'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Наименование', unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.DecimalField(blank=True, verbose_name='Старая цена', decimal_places=2, max_digits=9,
                                      default=0.0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(verbose_name='СКЮ', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=255, verbose_name='Адресная строка', unique=True,
                                   help_text='Уникальное значение в адресной строки для товара, добавляется автоматически.'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(verbose_name='Изменено', auto_now=True),
        ),
    ]
