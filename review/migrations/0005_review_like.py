# Generated by Django 3.0.8 on 2021-01-01 04:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('review', '0004_auto_20201226_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='like_review', to=settings.AUTH_USER_MODEL),
        ),
    ]
