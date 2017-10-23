# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20171020_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='title',
            field=models.CharField(default='title', max_length=200),
        ),
        migrations.AddField(
            model_name='work',
            name='image',
            field=models.ImageField(default='SOME STRING', upload_to=None),
        ),
        migrations.AddField(
            model_name='work',
            name='url',
            field=models.URLField(default='empty'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='mail',
            field=models.EmailField(max_length=254),
        ),
    ]
