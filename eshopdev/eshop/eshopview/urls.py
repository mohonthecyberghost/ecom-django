from django.contrib import admin
from django.urls import path

from eshopview import views

app_name = "eshopview"
urlpatterns = [
    path('', views.index, name='index'),
    path('cart-check/', views.cartCheck, name='cart'),


]
