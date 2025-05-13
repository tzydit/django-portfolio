from django.urls import path
from .views import django_info, contato_view, consulta_cep_view
from .views import aplicacoes, documentacao
urlpatterns = [
    path('', django_info, name='home'),
    path('contato/', contato_view, name='contato'),
    path('documentacao/', documentacao, name='documentacao'),
    path('aplicacoes/', aplicacoes, name='aplicacoes'),
    path('consulta_cep/', consulta_cep_view, name='cep'),

]
