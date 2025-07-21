#leitura de arquivos CSV PANDAS

import pandas as pd 
#instalar o openpyxl

#Definir caminho do CSV
caminho_csv = r"C:\\Users\\Giovana Cristina\Documents\\estudosarea\\EstudosArea\\Estudos Python\\alunos.csv"

#Definir caminho do Excel
caminho_excel = r"C:\\Users\\Giovana Cristina\Documents\\estudosarea\\EstudosArea\\Estudos Python\\alunos.xlsx"

#Extrair (LER) informações do arquivo CSV
# df = pd.read_csv('alunos.csv', sep = ",") #Dessa forma ele iria fazer a mesma leitura porém diretamente com o arquivo, sem o caminho pq ta na pasta
df = pd.read_csv(caminho_csv, sep = ",") #O sep vai separar em diferentes colunas o que estiver em aspas
print ("Leitura do arquivo CSV realizada com sucesso!")

#Salvar informações no excel
df.to_excel(caminho_excel, index = False)
print ("Arquivo excel salvo com sucesso")