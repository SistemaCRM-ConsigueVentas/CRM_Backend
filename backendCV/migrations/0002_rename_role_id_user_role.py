# Generated by Django 4.2.7 on 2023-11-17 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backendCV', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='role_id',
            new_name='role',
        ),
    ]
