# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170722_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weblog',
            name='post_words',
            field=models.CharField(max_length=100),
        ),
    ]
