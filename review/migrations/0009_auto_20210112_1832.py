# Generated by Django 3.0.8 on 2021-01-12 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0008_merge_20210106_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.TextField(default='', max_length=100),
        ),
    ]
