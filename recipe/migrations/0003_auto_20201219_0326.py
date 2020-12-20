# Generated by Django 3.0.8 on 2020-12-18 18:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_auto_20201005_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='count',
            field=models.PositiveIntegerField(default='', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
    ]