import pandas as pd
import numpy as np

caminho_csv = r"C:\\Users\\Giovana Cristina\Documents\\estudosarea\\EstudosArea\\Estudos Python\\alunos.csv"
caminho_csv_salvo = r"C:\\Users\\Giovana Cristina\Documents\\estudosarea\\EstudosArea\\Estudos Python\\alunos.csv"

df = pd.read_csv(caminho_csv)

print(df.head()) #5 primeiras linhas
print(df.columns) #quantidade de colunas
print(len(df)) #quantidade de linhas

#Filtre os alunos com nota maior que 7.0.
alunos_aprovados = df[df['nota'] > 7.0]
print (alunos_aprovados)

#Mostre a média das notas
media = df['nota'].mean() #Mean: calcula média aritmética de uma série de valores numéricos
print (f"{media:.2f}")

#Mostre todos os alunos da série do 9º ano
alunos_nono = df[df['série'] == "9º ano"]
print (alunos_nono)

#Adicione uma nova coluna chamada situação que mostre "Aprovado" se a nota for >= 7, senão "Reprovado".
df['situacao'] = np.where(df['nota'] >= 7, 'Aprovado', 'Reprovado') #“Se df['nota'] >= 7, escreva 'Aprovado', senão escreva 'Reprovado'”.
print(df[['nome', 'nota', 'situacao']])

#Salvar o arquivo
df.to_csv(caminho_csv, index= False)
print ("Arquivo salvo com sucesso")