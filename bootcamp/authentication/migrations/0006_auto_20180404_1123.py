# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-04 05:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20180404_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dead_kt',
            field=models.IntegerField(blank=True, default='NULL'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='live_kt',
            field=models.IntegerField(blank=True, default='NULL'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ten',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='tenpy',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twelve',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twelvepy',
            field=models.IntegerField(blank=True),
        ),
    ]
