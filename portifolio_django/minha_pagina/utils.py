import requests

def buscar_cep_via_api(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            dados = response.json()
            if 'erro' in dados:
                return {'erro': 'CEP não encontrado.'}
            return dados
        else:
            return {'erro': 'Erro ao consultar o CEP.'}
    except requests.exceptions.RequestException:
        return {'erro': 'Erro de conexão com a API do ViaCEP.'}
