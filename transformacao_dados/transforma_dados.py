import pdfplumber
import csv
#Extraia os dados da tabela Rol de Procedimentos e Eventos em Saúde do PDF do Anexo I

#acessar arquivo Anexo 1
pdf_caminho = "pdfs\Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"

#encontrar a tabela, percorrer as tabelas de cada página e extrair os dados.
tabelas = []
with pdfplumber.open(pdf_caminho) as pdf:
    for i in range(2,181):
        pagina_tabela = pdf.pages[i]
        #extrair os dados da tabela
        tabela = pagina_tabela.extract_table()

        if tabela:
            tabelas.extend(tabela) #pega todos os itens do laço for e adc na lista tabelas
            

with open("tabela_extraída.csv", mode="w", newline="", encoding="utf-8") as tab:
    writer = csv.writer(tab)
    for linha in tabelas:
        writer.writerow(linha)

print("Tabela extraída", tabelas)





