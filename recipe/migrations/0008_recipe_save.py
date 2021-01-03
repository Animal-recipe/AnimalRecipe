# Generated by Django 3.0.8 on 2021-01-01 05:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe', '0007_recipe_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='save',
            field=models.ManyToManyField(blank=True, related_name='save_recipe', to=settings.AUTH_USER_MODEL),
        ),
    ]