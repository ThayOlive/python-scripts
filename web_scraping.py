import requests
from bs4 import BeautifulSoup

#Acesso ao site
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
response = requests.get(url)

#Download dos Anexos I e II em formato pdf
#ler o HTML do site


#compactação de anexos em um unico arquivo ZIP