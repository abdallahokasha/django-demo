# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-30 19:19
from __future__ import unicode_literals

import datetime
from django.db import migrations
from django.utils.timezone import utc
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('landmarks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='landmark',
            name='country',
            field=django_countries.fields.CountryField(default=datetime.datetime(2018, 6, 30, 19, 19, 6, 524096, tzinfo=utc), max_length=2),
            preserve_default=False,
        ),
    ]
