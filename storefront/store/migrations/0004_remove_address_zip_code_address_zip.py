# Generated by Django 4.2.6 on 2023-10-24 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_address_zip_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.CharField(default='0000', max_length=10),
        ),
    ]
