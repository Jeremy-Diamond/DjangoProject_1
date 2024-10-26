# Generated by Django 5.1.2 on 2024-10-26 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0007_remove_goal_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='slug',
            field=models.SlugField(default='', max_length=200, unique=True),
        ),
    ]