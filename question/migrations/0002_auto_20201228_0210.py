# Generated by Django 3.0.8 on 2020-12-27 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ['-created', '-accept']},
        ),
        migrations.AddField(
            model_name='answer',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='question',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='accept',
            field=models.BooleanField(default=False),
        ),
    ]
