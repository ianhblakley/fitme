# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-20 16:30
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nutrition', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('total_calories', models.IntegerField()),
                ('total_carbohydrates', models.IntegerField()),
                ('total_fat', models.IntegerField()),
                ('total_protein', models.IntegerField()),
                ('total_vitamin_a', models.IntegerField()),
                ('total_vitamin_c', models.IntegerField()),
                ('total_iron', models.IntegerField()),
                ('total_calcium', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FoodLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('serving_count', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='meal',
            name='log',
        ),
        migrations.RemoveField(
            model_name='nutritionentry',
            name='meal',
        ),
        migrations.RemoveField(
            model_name='nutritionentry',
            name='serving',
        ),
        migrations.RemoveField(
            model_name='nutritionlog',
            name='user',
        ),
        migrations.AddField(
            model_name='food',
            name='log_count',
            field=models.BigIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Meal',
        ),
        migrations.DeleteModel(
            name='NutritionEntry',
        ),
        migrations.DeleteModel(
            name='NutritionLog',
        ),
        migrations.AddField(
            model_name='foodlog',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutrition.Food'),
        ),
        migrations.AddField(
            model_name='foodlog',
            name='serving',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutrition.Serving'),
        ),
        migrations.AddField(
            model_name='foodlog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
