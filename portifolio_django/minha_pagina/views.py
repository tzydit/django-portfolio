from django.shortcuts import render
from .forms import ContatoForm  # <-- necessário
from django.http import HttpResponse

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

