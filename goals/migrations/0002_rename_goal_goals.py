# Generated by Django 5.1.2 on 2024-10-19 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Goal',
            new_name='Goals',
        ),
    ]