#importações
import time
import requests
from googletrans import Translator

# Inicializar tradutor 
translator = Translator()

api_key = "e629c5dcb84047acbfcfa997a4ca115a"

pesquisa = "Google"

# Funcão para coletar as noticias
def dados():
    noticias_url = f"https://newsapi.org/v2/everything?q={pesquisa}&apiKey={api_key}"

    # Fazendo uma solicitação
    response = requests.get(noticias_url)

    # Convertendo os dados da resposta em JSON
    json_data = response.json()

    # Obtendo os primeiro artigos
    artigos = json_data["articles"][:5] # Limitado a 5 artigos

    titulos = []
    descricoes = []
    urls = []
    imagens = []

    for artigo in artigos:
        titulos.append(translator.translate(artigo['title']).text)

        descricoes.append(translator.translate(artigo['description']).text)

        urls.append(artigo['url'])

        imagens.append(artigo['urlToImage'])
    