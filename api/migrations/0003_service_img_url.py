# Generated by Django 3.2.23 on 2024-03-20 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20240320_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='img_url',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
