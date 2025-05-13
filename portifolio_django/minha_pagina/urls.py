from django.urls import path
from .views import django_info, contato_view, consulta_cep_view
from .views import aplicacoes, documentacao, filtrar_frameworks

urlpatterns = [
    path('', django_info, name='home'),
    path('contato/', contato_view, name='contato'),
    path('consulta_cep/', consulta_cep_view, name='cep'),
    path('documentacao/', documentacao, name='documentacao'),
    path('aplicacoes/', aplicacoes, name='aplicacoes'),
    path('filtrar_frameworks/', filtrar_frameworks, name='filtrar_frameworks')
]
