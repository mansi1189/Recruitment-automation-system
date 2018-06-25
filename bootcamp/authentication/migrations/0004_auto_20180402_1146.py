# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-02 06:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20180331_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='profile/mansi.jpg', upload_to='profile_pictures'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='passing_year',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
