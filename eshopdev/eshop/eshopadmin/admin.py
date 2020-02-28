from django.contrib import admin

# Register your models here.
from eshopadmin.models import itemCategory, product

admin.site.register(itemCategory)
admin.site.register(product)