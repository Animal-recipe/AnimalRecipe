# Generated by Django 3.0.8 on 2020-12-22 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footer', '0003_auto_20201222_1636'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report_problem',
            old_name='username',
            new_name='author',
        ),
        migrations.AlterField(
            model_name='report_problem',
            name='reason',
            field=models.CharField(default='', max_length=100),
        ),
    ]
