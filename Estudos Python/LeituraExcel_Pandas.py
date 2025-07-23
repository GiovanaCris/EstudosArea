#Importação de bibliotecas
import pandas as pd 

#Ler arquivo excel
df = pd.read_excel(
    r"Estudos Python\\alunosExcel.xlsx",
    sheet_name="Sheet1", #Nome da aba que eu quero
    skiprows=1, #Quantidade de linhas que pula para chegar lá
    usecols=["nome", "nota"] #Colunas que eu quero importar
) #Aqui eu copiei o caminho clicando no mouse direito e copiando direto o caminho do arquivo
df

#Dropar valores NaN
df = df.dropna()
df

#Setar coluna de Fornecedor como Índice (transforma o índice padrão em uma coluna da tabela)
df = df.set_index("nota")
df

#Exportar tabela
df.to_excel("testetabela.xlsx")