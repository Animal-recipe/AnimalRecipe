# Generated by Django 3.1.3 on 2020-12-01 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20201201_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='nickname', max_length=20, unique=True, verbose_name='nickname'),
        ),
        migrations.AlterField(
            model_name='user',
            name='petname',
            field=models.CharField(default='petname', max_length=20, verbose_name='petname'),
        ),
    ]
