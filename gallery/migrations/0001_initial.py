# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='media/images/main')),
                ('caption', models.CharField(blank=True, max_length=250)),
                ('item', models.ForeignKey(to='gallery.Item')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
