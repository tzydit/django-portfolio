from django.urls import path
from . import views

urlpatterns = [
    path('', views.django_info, name='home'),  # Essa rota é para /
]
