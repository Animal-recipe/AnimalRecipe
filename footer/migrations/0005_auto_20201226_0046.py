# Generated by Django 3.0.8 on 2020-12-25 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('footer', '0004_auto_20201222_1650'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report_problem',
            old_name='name',
            new_name='target',
        ),
    ]
