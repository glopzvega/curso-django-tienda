# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(default=0),
        ),
    ]
