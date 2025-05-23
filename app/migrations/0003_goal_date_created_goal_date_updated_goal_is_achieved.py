# Generated by Django 5.1.2 on 2024-12-31 19:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_goal_name_goal'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goal',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='goal',
            name='is_achieved',
            field=models.BooleanField(default=False),
        ),
    ]
