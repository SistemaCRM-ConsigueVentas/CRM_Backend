# Generated by Django 4.2.7 on 2023-11-27 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendCV', '0012_client_invoice_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
