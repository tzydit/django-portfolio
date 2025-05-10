from django.shortcuts import render
from .forms import ContatoForm
from django.http import HttpResponse
from .utils import buscar_cep_via_api  # função para consumir a API do ViaCEP


def contato_view(request):
    enviado = False
    dados = None

    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            dados = form.cleaned_data
            enviado = True
    else:
        form = ContatoForm()

    return render(request, 'minha_pagina/contato.html', {
        'form': form,
        'enviado': enviado,
        'dados': dados
    })


def django_info(request):
    return render(request, 'minha_pagina/django_info.html')


def consulta_cep_view(request):
    resultado = None
    if request.method == 'POST':
        cep = request.POST.get('cep', '').replace('-', '').strip()
        if cep:
            resultado = buscar_cep_via_api(cep)
    return render(request, 'minha_pagina/consulta_cep.html', {'resultado': resultado})
