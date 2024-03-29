# Generated by Django 3.1.3 on 2020-12-01 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_user_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.ImageField(blank=True, default='profiles/default.PNG', null=True, upload_to='profiles/', verbose_name='profile'),
        ),
    ]
