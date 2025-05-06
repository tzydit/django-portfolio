from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('minha_pagina.urls')),  # A raiz aponta para o app
]
