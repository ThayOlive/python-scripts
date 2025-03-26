import requests
from web_scraping import response, arquivos

#função para testar acesso ao site 
def acesso_ao_site():
    if response.status_code == 200:
        print("Url acessada com sucesso!")
    else:
        print("Erro ao acessar a url", response.status_code)#retornar resposta da requisição
acesso_ao_site()

