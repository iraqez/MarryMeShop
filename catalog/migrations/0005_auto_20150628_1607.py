# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20150628_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(help_text='Уникальное имя для отображения в адресе(заполнять без пробелов и латиницей)', verbose_name='Адресная строка', unique=True),
        ),
    ]
