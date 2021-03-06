# Generated by Django 2.2 on 2020-01-04 18:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=200)),
                ('PersonName', models.CharField(max_length=200)),
                ('contractNumber', models.CharField(max_length=200)),
                ('image', models.FileField(upload_to='image/')),
                ('bankAccount', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('emailAddress', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
