# Generated by Django 2.2 on 2020-01-07 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20200105_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyregistration',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='document/company'),
        ),
    ]
