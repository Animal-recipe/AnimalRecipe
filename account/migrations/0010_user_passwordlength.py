# Generated by Django 3.0.8 on 2021-01-01 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20201224_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='passwordLength',
            field=models.SmallIntegerField(default=0),
        ),
    ]