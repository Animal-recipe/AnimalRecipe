# Generated by Django 3.0.8 on 2020-12-25 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_remove_review_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review_img',
            name='image',
            field=models.ImageField(blank=True, upload_to='review_img/%Y/%m/%d'),
        ),
    ]
