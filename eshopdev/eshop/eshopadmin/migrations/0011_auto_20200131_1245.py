# Generated by Django 2.2 on 2020-01-31 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshopadmin', '0010_auto_20200131_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.FileField(blank=True, null=True, upload_to='document/company'),
        ),
    ]