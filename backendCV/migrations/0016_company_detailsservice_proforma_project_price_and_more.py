# Generated by Django 4.2.7 on 2023-12-06 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backendCV', '0015_rename_expense_status_expensestatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('business_name', models.CharField(max_length=255)),
                ('tax_id', models.CharField(max_length=15)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=255)),
                ('website', models.CharField(max_length=50)),
                ('office_address', models.CharField(max_length=255)),
                ('portfolio', models.CharField(max_length=50)),
            ],
        ),

    ]