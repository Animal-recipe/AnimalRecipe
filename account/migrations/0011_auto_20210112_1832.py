# Generated by Django 3.0.8 on 2021-01-12 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_user_passwordlength'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='petkind',
            field=models.CharField(choices=[('DOG', '개'), ('CAT', '고양이'), ('RAB', '토끼'), ('BIRD', '새'), ('FISH', '물고기'), ('HAM', '햄스터'), ('ETC', '기타'), ('NONE', '없음')], max_length=4),
        ),
        migrations.AlterField(
            model_name='user',
            name='petname',
            field=models.CharField(blank=True, default='petname', max_length=20, null=True, verbose_name='petname'),
        ),
    ]
