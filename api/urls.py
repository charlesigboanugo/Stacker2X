from django.contrib import admin
from django.urls import path
from .views import classifyNum

urlpatterns = [
    path('classify-number', classifyNum),
]