#Filtrar colunas por tipos de dados
import pandas as pd

df = pd.DataFrame([
    [1,2, True, 1.2],
    ['a', 2, False, 1.4],
    ['v', 3, True, 1.6],
    [True, 3, False, 1.8],
    [3.5, 4, True, 2.0]
], columns=['col1', 'col2', 'col3', 'col4'])

print(df.select_dtypes(include=['int64', 'bool'])) #Vai mostrar as que tem esse valor
print(df.select_dtypes(exclude=['int64', 'bool'])) #Vai mostrar as que não tem esse valor

isinstance(True, bool) #Recebe dois valores o primeiro é o valor e o segundo é oq a gnt quer verificar se é uma instancia
print(df[df['col1'] == True])

print(df[df['col1'].apply(lambda x: isinstance(x, bool))]) #Vai filtrar nesse caso, tudo da linha 3 com valor booleano
