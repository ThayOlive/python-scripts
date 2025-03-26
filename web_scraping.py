import requests
from bs4 import BeautifulSoup

#Acesso ao site
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
response = requests.get(url)

#Download dos Anexos I e II em formato pdf
#ler o HTML do site
soup = BeautifulSoup(response.text, "html.parser")
links = soup.find_all("a", href = True)

#buscando os arquivos na página
arquivos = []
for link in links:
    if link["href"].endswith(".pdf") and "Anexo_I" in link["href"] or "Anexo_II" in link["href"]:
        arquivos.append(link["href"])
print(arquivos)




#compactação de anexos em um unico arquivo ZIP