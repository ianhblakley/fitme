# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-13 19:15
from __future__ import unicode_literals

from django.db import migrations, models

import supplementation.models


class Migration(migrations.Migration):
    dependencies = [
        ('supplementation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplement',
            name='label',
            field=models.ImageField(blank=True, default=None, upload_to=supplementation.models.get_label_path),
        ),
    ]
