# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20171022_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='SOME STRING', upload_to='static/website'),
        ),
    ]
