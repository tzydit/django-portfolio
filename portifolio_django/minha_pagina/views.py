from django.shortcuts import render
from .forms import ContatoForm
from django.http import HttpResponse
from django.shortcuts import render
from .utils import buscar_cep_via_api 


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

def buscar_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()  
        else:
            return {"erro": "Erro na consulta do CEP."}  
    except requests.exceptions.RequestException as e:
        return {"erro": f"Erro ao conectar com a API: {str(e)}"} 



def django_info(request):
    return render(request, 'minha_pagina/django_info.html')

def documentacao(request):
    return render(request, 'minha_pagina/documentacao.html')

def aplicacoes(request):
    return render(request, 'minha_pagina/aplicacoes.html')

def consulta_cep_view(request):
    resultado = None
    if request.method == 'POST':
        cep = request.POST.get('cep', '').replace('-', '').strip() 
        if cep:
            resultado = buscar_cep_via_api(cep)  
    return render(request, 'minha_pagina/consulta_cep.html', {'resultado': resultado})

