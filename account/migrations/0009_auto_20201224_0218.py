# Generated by Django 3.1.3 on 2020-12-23 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20201202_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.ImageField(blank=True, default='profiles/defaultProfile.png', null=True, upload_to='profiles/', verbose_name='profile'),
        ),
    ]
