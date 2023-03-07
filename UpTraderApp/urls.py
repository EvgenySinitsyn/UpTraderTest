from django.contrib import admin
from .views import index, menu
from django.urls import path, include

urlpatterns = [
    path('', index, name='index'),
    path('<slug:slug>/', menu, name='menu'),
]