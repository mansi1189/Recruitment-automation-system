# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-31 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20180331_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='live_kt',
            field=models.IntegerField(blank=True, default='NULL'),
        ),
    ]
