"""
Naivas URL Configuration

The `urlpatterns` list routes URLs to views.
"""
from django.contrib import admin
from django.urls import include, path


admin.site.site_header = 'Naivas Admin'
admin.site.index_title = 'Admin'

urlpatterns = [
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),
]
