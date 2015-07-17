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
            options={'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии', 'ordering': ['title']},
        ),
        migrations.AddField(
            model_name='photo',
            name='number',
            field=models.IntegerField(verbose_name='Номер показа', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='caption',
            field=models.CharField(blank=True, verbose_name='Описание', max_length=250),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=gallery.fileds.ThumbnailImageField(verbose_name='Фото', upload_to='media/images/main/tovar'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(verbose_name='Название', max_length=100),
        ),
    ]
