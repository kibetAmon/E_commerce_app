"""
Naivas URL Configuration

The `urlpatterns` list routes URLs to views.
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),
]
