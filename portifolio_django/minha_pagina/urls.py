from django.urls import path
from . import views

urlpatterns = [
    path('django_info/', views.django_info, name='django_info'),
]
