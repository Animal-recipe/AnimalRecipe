# Generated by Django 3.0.8 on 2021-01-03 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0009_auto_20210101_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='summary',
            field=models.TextField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.TextField(default='', max_length=20),
        ),
    ]
