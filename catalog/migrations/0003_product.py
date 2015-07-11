# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20150628_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('slug', models.SlugField(help_text='Unique value for product page URL, created automatically from name.', unique=True, max_length=255)),
                ('brand', models.CharField(max_length=50)),
                ('sku', models.CharField(max_length=50)),
                ('price', models.DecimalField(max_digits=9, decimal_places=2)),
                ('old_price', models.DecimalField(blank=True, max_digits=9, default=0.0, decimal_places=2)),
                ('is_active', models.BooleanField(default=True)),
                ('is_bestseller', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('quantity', models.IntegerField()),
                ('description', models.TextField()),
                ('meta_keywords', models.CharField(verbose_name='Meta Keywords', max_length=255, help_text='Comma-delimited set of SEO keywords for keywords meta tag')),
                ('meta_description', models.CharField(verbose_name='Meta Description', max_length=255, help_text='Content for description meta tag')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='images/products/main')),
                ('thumbnail', models.ImageField(upload_to='images/products/thumbnails')),
                ('image_caption', models.CharField(max_length=200)),
                ('categories', models.ManyToManyField(to='catalog.Category')),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'products',
            },
        ),
    ]
