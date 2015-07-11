# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import gallery.fileds


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name_plural': 'Фотографии', 'verbose_name': 'Фотография'},
        ),
        migrations.RemoveField(
            model_name='photo',
            name='title',
        ),
        migrations.AlterField(
            model_name='photo',
            name='caption',
            field=models.CharField(max_length=250, blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=gallery.fileds.ThumbnailImageField(upload_to='media/images/main', verbose_name='Фото'),
        ),
    ]
