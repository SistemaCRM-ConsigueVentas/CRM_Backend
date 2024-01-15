# Generated by Django 3.2.23 on 2024-01-11 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_client_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='document_number',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='document_type',
            field=models.CharField(choices=[(0, 'DNI'), (1, 'CEDULA'), (2, 'PASAPORTE'), (3, 'OTRO')], default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]