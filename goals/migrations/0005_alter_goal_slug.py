# Generated by Django 5.1.2 on 2024-10-26 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0004_goal_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='slug',
            field=models.SlugField(max_length=75, unique=True),
        ),
    ]