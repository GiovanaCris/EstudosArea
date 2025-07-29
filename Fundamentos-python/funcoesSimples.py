#Função -> Bloco de código reutilizável garatindo a organização

def calcular_imposto(valor):
    if valor < 1000:
        imposto = valor * 0.1
    elif valor < 2000:
        imposto = valor * 0.13
    else:
        imposto = valor * 0.2
    
    return imposto

preco_produto1 = 1500
preco_produto2 = 3500
imposto_produto1 = calcular_imposto(preco_produto1)
imposto_produto2 = calcular_imposto(preco_produto2)
print(imposto_produto1)
print(imposto_produto2)

#Exercício 1 - Fatorial de um número
def fatorial_numero(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial = fatorial * i
    return fatorial

numero = 7
resultado = fatorial_numero(numero)
print (f"\nO resultado desse cálculo é: {resultado}")

#Exercício 2 - contar vogais
def contar_vogais(palavra):
    contador = 0
    palavra = palavra.lower()
    vogais = "aeiou"
    for i in palavra:
        if i in vogais:
            contador += 1
    return contador
            
palavra = "giovana"
resultado = contar_vogais(palavra)
print (f"{palavra} tem {resultado} vogais")

#Exercício 3 - Palíndromo
def palindromo(palavra):
    palavra = palavra.lower()
    palavra_invertida = palavra[::-1] #Operação de fatiamento, faz uma cópia da sequência original porém na ordem inversa
    if palavra_invertida == palavra:
        print (f"\n{palavra_invertida} é um palíndromo")
    else:
        print (f"\n{palavra} não é um palíndromo")

palavra = "ana"
palindromo(palavra)