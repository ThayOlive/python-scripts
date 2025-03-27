import pdfplumber
import csv
import os
import shutil
#Extraia os dados da tabela Rol de Procedimentos e Eventos em Saúde do PDF do Anexo I

#acessar arquivo Anexo 1
pdf_caminho = "pdfs\Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"

abreviacoes = {
    "OD": "Seg.Odontológica",
    "AMB": "Seg.Ambulatorial"
}

#encontrar a tabela, percorrer as tabelas de cada página e extrair os dados.
tabelas = []
with pdfplumber.open(pdf_caminho) as pdf:
    for i in range(2,181):
        pagina_tabela = pdf.pages[i]
        #extrair os dados da tabela
        tabela = pagina_tabela.extract_table()

        if tabela:
            # substituir abreviações na tabela
            for linha in tabelas:
                for j, valor in enumerate(linha):
                    if valor in abreviacoes:
                        linha[j] = abreviacoes[valor]
        print('Fazendo o tratamento dos dados, aguarde uns minutos...')
        
        tabelas.extend(tabela) #pega todos os itens do laço for e adc na lista tabelas
print('Tratamento feito!')
os.makedirs('csv', exist_ok=True)

caminho_csv = os.path.join('csv', 'tabela_extraída.csv')

#salvar as tabelas em formato csv
with open(caminho_csv, mode="w", newline="", encoding="utf-8") as tab:
    writer = csv.writer(tab)
    for linha in tabelas:
        writer.writerow(linha)

print(f"Tabela extraída e abreviações substituídas, arquivo salvo em {caminho_csv}")

#Compacte o csv em um arquivo denominado "Teste_{seu_nome}.zip".

nome_arquivo_zip = "Teste_thayla_oliveira"
shutil.make_archive(nome_arquivo_zip, 'zip', 'csv', 'tabela_extraída.csv')

print(f'Arquivo {nome_arquivo_zip} compactado com sucesso! ')









