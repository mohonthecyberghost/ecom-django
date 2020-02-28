from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class CompanyRegistration(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    companyName = models.CharField(max_length=200)
    PersonName = models.CharField(max_length=200)
    contractNumber = models.CharField(max_length=200)
    image = models.FileField(upload_to='document/company', blank=True, null=True)
    bankAccount = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    emailAddress = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.companyName
