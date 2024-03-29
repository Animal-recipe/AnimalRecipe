# Generated by Django 3.0.8 on 2020-09-28 09:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Remessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentAt', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(max_length=150)),
                ('isRead', models.BooleanField(default=False)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remessage', to='contact.Message')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remessage_receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remessage_sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-sentAt'],
            },
        ),
    ]
