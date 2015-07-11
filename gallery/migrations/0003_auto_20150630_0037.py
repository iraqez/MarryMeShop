# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20150630_0034'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': 'Фотография', 'ordering': ['title'], 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.AddField(
            model_name='photo',
            name='title',
            field=models.CharField(default=1, verbose_name='Название', max_length=100),
            preserve_default=False,
        ),
    ]
