from django.urls import path
from .views import django_info, contato_view, documentacao
from .views import aplicacoes


urlpatterns = [
    path('', django_info, name='home'),
    path('contato/', contato_view, name='contato'),
    path('documentacao/', documentacao, name='documentacao'),
    path('aplicacoes/', aplicacoes, name='aplicacoes'),
]
