# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import gallery.fileds


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20150630_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='number',
            field=models.IntegerField(verbose_name='Номер показа', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=gallery.fileds.ThumbnailImageField(upload_to='media/images/main/tovar', verbose_name='Фото'),
        ),
    ]
