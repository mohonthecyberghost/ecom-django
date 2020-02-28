from django.db import models


# Create your models here.
class itemCategory(models.Model):
    categoryName = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.categoryName


class product(models.Model):
    itemCategory_id = models.ForeignKey(itemCategory, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_code = models.CharField(max_length=200)
    product_price = models.CharField(max_length=200)
    product_total = models.CharField(max_length=200)
    product_detail = models.CharField(max_length=200)
    product_company = models.CharField(max_length=200)
    product_discount = models.CharField(max_length=200)
    product_image = models.FileField(upload_to='document/company', blank=False, null=False, editable=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
