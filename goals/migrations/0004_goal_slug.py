# Generated by Django 5.1.2 on 2024-10-26 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0003_rename_goals_goal'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='slug',
            field=models.SlugField(default='slug', max_length=75, unique=True),
        ),
    ]
