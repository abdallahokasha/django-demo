# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-30 23:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landmarks', '0007_auto_20180630_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landmark',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
