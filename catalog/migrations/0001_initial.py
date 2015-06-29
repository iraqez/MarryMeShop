# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('first_menu', models.CharField(choices=[('a', 'Для невесты'), ('b', 'Для жениха'), ('c', 'Для автомобиля'), ('d', 'Для детей'), ('e', 'Аксессуары')], max_length=30)),
                ('name', models.CharField(unique=True, verbose_name='Название', max_length=50)),
                ('slug', models.SlugField(unique=True, verbose_name='Адресная строка', help_text='Уникальное имя для отображения в адресе(заполнять без пробелов и латиницей)')),
                ('description', models.TextField(verbose_name='Описание')),
                ('is_active', models.BooleanField(verbose_name='Активно', default=True)),
                ('meta_keywords', models.CharField(verbose_name='Ключи', help_text='ключевые слова для СЕО поисковых запросов', max_length=255)),
                ('meta_description', models.CharField(verbose_name='Метатеги', help_text='Метатеги для поиска контента', max_length=255)),
                ('created_at', models.DateTimeField(verbose_name='Создано', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='Изменено', auto_now=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'db_table': 'categories',
                'verbose_name_plural': 'Категории',
                'ordering': ['-created_at', 'first_menu'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('item_ptr', models.OneToOneField(primary_key=True, parent_link=True, serialize=False, to='gallery.Item', auto_created=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('slug', models.SlugField(unique=True, help_text='Unique value for product page URL, created automatically from name.', max_length=255)),
                ('brand', models.CharField(max_length=50)),
                ('sku', models.CharField(max_length=50)),
                ('price', models.DecimalField(max_digits=9, decimal_places=2)),
                ('old_price', models.DecimalField(max_digits=9, blank=True, decimal_places=2, default=0.0)),
                ('is_active', models.BooleanField(default=True)),
                ('is_bestseller', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('quantity', models.IntegerField()),
                ('description', models.TextField()),
                ('meta_keywords', models.CharField(verbose_name='Meta Keywords', help_text='Comma-delimited set of SEO keywords for keywords meta tag', max_length=255)),
                ('meta_description', models.CharField(verbose_name='Meta Description', help_text='Content for description meta tag', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(to='catalog.Category')),
            ],
            options={
                'db_table': 'products',
                'ordering': ['-created_at'],
            },
            bases=('gallery.item',),
        ),
    ]
