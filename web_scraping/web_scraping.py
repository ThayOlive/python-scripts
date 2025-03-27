import requests
from bs4 import BeautifulSoup
import os
import shutil

#Acesso ao site
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
response = requests.get(url)


#ler o HTML do site
soup = BeautifulSoup(response.text, "html.parser")
links = soup.find_all("a", href = True)

#buscando os arquivos na página
arquivos = []
for link in links:
    if link["href"].endswith(".pdf") and "Anexo_I" in link["href"] or "Anexo_II" in link["href"]:
        arquivos.append(link["href"])
print(arquivos)

#criar uma pasta para salvar os anexos
os.makedirs('pdfs', exist_ok=True)

#baixar e salvar anexos
for arquivo_url in arquivos:
    nomeArquivo = os.path.join("pdfs", arquivo_url.split("/")[-1])
    print(f'Baixando {nomeArquivo}')

    response =requests.get(arquivo_url)

    with open(nomeArquivo, "wb") as arquivo:
        arquivo.write(response.content)

    print(f"Download concluído: {nomeArquivo}")

#compactação de anexos em um unico arquivo ZIP
zip_nome = "anexos_compactados"
pasta_anexos = "pdfs"

shutil.make_archive(zip_nome, 'zip', pasta_anexos)
