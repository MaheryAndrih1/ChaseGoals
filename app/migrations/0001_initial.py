# Generated by Django 5.1.2 on 2024-12-31 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id_goal', models.AutoField(primary_key=True, serialize=False)),
                ('name_goal', models.CharField(max_length=25)),
            ],
        ),
    ]
