#Criar estrutura para relatório em python

from fpdf import FPDF #Módulo de arquivo PDF
import matplotlib.pyplot as plt #Criação de gráficos
from numpy.random import seed, randint #Gerar dados aleatórios
from pandas import DataFrame #Trabalhar com tabelas

#Criar dados
seed(42) #Semente para ter controle dos dados

df0 = DataFrame() #Tabela do python
df0['loja'] = [c for c in 'ABCDE' for _ in range(12)] #coluna loja, lista que guarda ABCDE separadamente em cada uma das linhas 12 vezes, ou seja A 12 vezes, B 12 vezes...
df0['mes'] = [i+1 for _ in range(5) for i in range(12)] #coluna mês, números de 1 a 12 eem cada unma das linhas
df0[2024] = randint(15_000, 25_000, len(df0)) #coluna 2024 #Na coluna 2024 e 2025 vai gerar um número aleatório nos campos através da biblioteca randint
df0[2025] = randint(15_000, 25_000, len(df0)) #coluna 2025
df0

#Criar figura
lojas = df0['loja'].unique() #Pega uma loja de cada vez, os valores únicos da coluna df0
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'] #Cada um dos meses que aparece embaixo do frame
#Mudar a cor
plt.style.use('dark_background') #Cor do fundo do gráfico
#Alterar fonte
plt.rc('font', size=15) #plt = valor padrão
#Criar a figura dos gráficos
fig = plt.figure(figsize=(21, 29.7)) #Fica no tamanho certinho do pdf, nesse caso tem o tamanho de uma folha A4
#Titulo principal
fig.suptitle('Hello World, tabela da gi', size=30, y=0.995) #Meu título no tamanho da fonte 30 na altura da tela de qse 1 milimetro
#Largura das barras do gráfico
largura = 0.35 #Importante para deslocar as barrinhas e não deixar uma encima da outra

for i, loja in enumerate(lojas, start=1): #Cria cada um dos pares de eixo do gráfico, o start = 1 é para não dar erro pois a posição do gráfico começa em 1
    print(i, loja)
    
    #Só as linhas da loja A, só as linhas da loja B e por ai vai
    df = df0[df0['loja'] == loja] #df é igual a df 0 onde loja é igual a variável loja #Filtra a tabela original com todas as tabelas para cada uma das lojas
    
    ax = fig. add_subplot(len(lojas), 1, i) #quantos gráficos eu quero criar, a quantidade de gráficos vai ser igual a de  lojas len(lojas) e as colunas vão ser 1 única coluna e esse gráfico vai estar na posição 1
    ax.set_title(f'Loja {loja}', size=20) #Titulo de cada um dos eixos da tabela no tamanho de 20
    
    #Criar de fato o gráfico de barra
    barras1 = ax.bar(df['mes']- largura/2, df[2024], width=largura, color='yellow') #minha coluna de mes vai ter a altura do número de 2024 respectivo #O LARGURA / 2 VAI FAZER FICAR DO LADO E NÃO SOBREPOSTO 
    barras2 = ax.bar(df['mes']+ largura/2, df[2025], width=largura, color= 'gold') #minha coluna de mes vai ter a altura do número de 2025 respectivo  #O LARGURA / 2 VAI FAZER FICAR DO LADO E NÃO SOBREPOSTO 
    
    ax.bar_label(barras1, fmt='{:,.0f}', size=12) #Númmero encima de cada uma das barrinhas
    ax.bar_label(barras2, fmt='{:,.0f}', size=12)
    
    ax.set_yticks([0, ax.get_ylim()[1]*1.2]) #Dar um espaço para os anos do glossário não ficarem encima do gráfico
    
    ax.set_xticks(df['mes'], meses) #Nas cordenadas do mes, colocar os nomes dos meses (variavel meses)
    ax.set_yticks([]) #Tira os valores que estavam do lado com um eixo vazio
    
    #Calculo de diferença de comparação do gráfico
    for index in df.index: 
        porcentagem = df.loc[index, 2025] / df.loc[index, 2024] - 1
        
        if porcentagem > 0: #cor fica vede
            cor = (0,0.8, 0)
        else:
            cor = (0.8, 0, 0) #cor fica vermelha

        ax.text(
            df.loc[index, 'mes'],
            ax.get_ylim()[1] * 0.1,
            f'{porcentagem:+.0%}',
            ha = 'center',
            va = 'center',
            bbox = dict(fc=cor)
        )
        
    ax.legend([2024, 2025])
    
fig.tight_layout() #Formatação melhor de enquadramento

#Salvar a figura do PDF
fig.savefig('Hello World, tabela da gi')

#Criar PDF
pdf = FPDF()
pdf.add_page()
pdf.image('Hello World, tabela da gi.png', 0, 0, 21, 0) #Coloca a imagem no PDF #cordenadas: x = 0; y = 0; largura da imagem = 210mm; altura = 0 (usa as proporções normais da figura criada)
pdf.output('relatórioGi.pdf')