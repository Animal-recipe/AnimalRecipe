# Generated by Django 3.0.8 on 2020-12-18 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_auto_20201219_0326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='count',
        ),
    ]