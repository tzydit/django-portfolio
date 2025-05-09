from django.urls import path
from .views import django_info, contato_view

urlpatterns = [
    path('', django_info, name='home'),
    path('contato/', contato_view, name='contato'),
]
