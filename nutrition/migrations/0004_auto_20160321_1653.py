# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-21 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0003_goal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='date_set',
            field=models.DateField(auto_now=True),
        ),
    ]
