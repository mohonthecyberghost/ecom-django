from django.contrib import admin
from django.urls import path

from registration import views

app_name = "registration"
urlpatterns = [
    path('', views.index, name='index'),
    path('companyRegistration/', views.companyRegistration, name='companyRegistration'),
    path('companyLogin/', views.companyLogin, name='companyLogin'),
    path('login/', views.login, name='login'),
]
