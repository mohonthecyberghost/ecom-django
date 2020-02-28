from django.contrib import admin
from django.urls import path

from eshopadmin import views

app_name='eshopadmin'
urlpatterns = [
    path('', views.index, name='index'),
    path('manageItemCategory/', views.manageItemCategory, name='manageItemCategory'),
    path('itemCategoryDelete/<int:id>', views.itemCategoryDelete, name='itemCategoryDelete'),
    # path('ItemCategoryEdit/', views.ItemCategoryEdit, name='ItemCategoryEdit'),
    path('editItemCategory/', views.editItemCategory, name='editItemCategory'),
    path('productManage/', views.productManage, name='productManage'),
    path('productEdit/', views.productEdit, name='productEdit'),
    path('productDelete/<int:id>', views.productDelete, name='productDelete'),



]
