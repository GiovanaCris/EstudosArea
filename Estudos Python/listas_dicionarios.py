#>>>>>>>>>>>>> LISTAS <<<<<<<<<<<<<<
#Printar o valor de uma lista
mercado = [
    'arroz',
    'feijao',
    'batata',
    'tomate',
    'chocolate',
    'brocolis',
    'cebola',
    'cebola'
]

print (mercado[1])

#Remover duplicados de uma lista
mercado = list(set(mercado)) #Set vai tirar o repetido e deixar único, o list é para converter o diciocionáiro do set em uma lista
print (mercado)

#Adicionar valor em uma lista
mercado.append('moranguinhoss') #append vai fazer a edição de um novo produto no nosso mercado
print (mercado)

# mercado.insert(0, 'moranguinoss') #O insert vai tornar possível a adição do produto especificando o índice que queremos
# print (mercado)

#>>>>>>>>>>> DICIONÁRIOS <<<<<<<<<<<
#Printar o valor de um dicionário
mercado = {
    'entrada': 'chocolate', #As chaves ssão valores únicos
    'saida': 'moranguinhos'
}
print (mercado['entrada']) #Ao invés de  buscar pelo índice, busca pela chave

#Remover item de um dicionário
mercado.pop('entrada') #O pop vai remover a chave citada
print (mercado)

#Adicionar valor em um dicionário
mercado['entrada'] = 'chocolate branco'
print (mercado)

#Lista dentro de um dicionário
mercado['entrada'] = ['leite em pó', 'brigadeiro']
mercado['saida'] = ['ganache', 'bombom']
print (mercado['entrada'])
print (mercado['entrada'][0]) #Pego o índece 0 da lista de entrada