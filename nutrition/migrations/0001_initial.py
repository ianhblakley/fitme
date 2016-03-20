# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-17 18:02
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('barcode', models.IntegerField(default=0)),
                ('calories_per_100g', models.IntegerField()),
                ('carbohydrates_per_100g', models.IntegerField()),
                ('fat_per_100g', models.IntegerField()),
                ('protein_per_100g', models.IntegerField()),
                ('vitamin_a_per_100g', models.IntegerField()),
                ('vitamin_c_per_100g', models.IntegerField()),
                ('iron_per_100g', models.IntegerField()),
                ('calcium_per_100g', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='NutritionEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_servings', models.FloatField()),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutrition.Meal')),
            ],
        ),
        migrations.CreateModel(
            name='NutritionLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
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
            name='Serving',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('scalar', models.FloatField()),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutrition.Food')),
            ],
        ),
        migrations.AddField(
            model_name='nutritionentry',
            name='serving',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutrition.Serving'),
        ),
        migrations.AddField(
            model_name='meal',
            name='log',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutrition.NutritionLog'),
        ),
    ]
