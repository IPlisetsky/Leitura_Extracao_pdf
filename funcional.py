import os
import pdfplumber
import pandas as pd
import time

# Definindo diretórios
diretorio_atual = os.getcwd()
print(diretorio_atual)

diretorio_arquivos = r"Diretorio"

# Processando arquivos PDF
lista_arquivos = os.listdir(diretorio_arquivos)
data = []  # Lista para armazenar os dados extraídos
erro = []  # Lista para armazenar erros encontrados

# Le todos os arquivos da lista
for arquivo in lista_arquivos:
    if ".pdf" not in arquivo:
        continue  # Ignora arquivos que não sejam PDF

    try:
        # Abrindo o PDF
        with pdfplumber.open(f"{diretorio_arquivos}/{arquivo}") as pdf:
            pagina = pdf.pages[0] # Seleciona a pagina que será lida
            texto = pagina.extract_text() # Extrai texto da pagina
            linhas = texto.split("\n") # Separa as linhas
            a = 0

            # LINHA CÓDIGO
            # EXEMPLO
            for i, linha in enumerate(linhas):               
                if "CÓDIGO" in linha:
                    print(f"ENCONTRADO NA LINHA {i}")
                    colunas = linhas[i].split(" ") # Exemplo de coluna de valores
                    valores = linhas[i + 1].split(" ") # Linha de valores
                  
                    variavel_exemplo = valores[2]
                    
                    # Armazenando dados em um dicionário
                    data_linha = {
                        "ARQUIVO": arquivo,
                        "COLUNA1": variavel_exemplo
                    }
                    data.append(data_linha)

    except Exception as e:
        print(f"ERRO no arquivo {arquivo}: {e}")
        erro.append(arquivo)

# Criando e salvando o DataFrame
df_erro = pd.DataFrame(erro)
df_erro.to_excel(f"{diretorio_atual}\erros.xlsx", index = False)
df = pd.DataFrame(data)
df.to_excel(f"{diretorio_atual}\dados.xlsx", index=False)
print("\nPlanilha dados.xlsx gerada!\n")
print("\nPlanilha erros.xlsx gerada!\n")
