"""
Naivas URL Configuration

The `urlpatterns` list routes URLs to views.
"""
from django.contrib import admin
from django.urls import include, path
from . import settings
from django.conf.urls.static import static


admin.site.site_header = 'Naivas Admin'
admin.site.index_title = 'Admin'

urlpatterns = [
    path('home/', include('home.urls')),
    path('', include('store.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
