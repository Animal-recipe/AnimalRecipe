# Generated by Django 3.0.8 on 2021-01-03 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0006_review_hits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.TextField(default='', max_length=20),
        ),
    ]
