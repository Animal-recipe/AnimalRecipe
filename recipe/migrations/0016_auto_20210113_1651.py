# Generated by Django 3.0.8 on 2021-01-13 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0015_auto_20210112_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='animal',
            field=models.CharField(default='', max_length=10),
        ),
    ]