#FOR
#Números de 1 a 100 com for range
for i in range(1, 101): 
    print (i)
    
#For com listas
frutas = ['morango', 'uva', 'abacaxi']
for fruta in frutas: #Vai percorrer a lista e cada item vai mandar para a variável fruta
    print(fruta)
    
#For com string
for letra in "Giovana":
    print(letra)

#Somar números
somar = 0 #Cria a variável soma que inicia em 0
for n in range(1, 11): #Um loop que  vai ser executado 10 vezes
    somar += 1 #Nas 10 vezes acrescenta um valor na variável soma
print (f"A soma total é {somar}")

#WHILE
#Mostra os valores do contador
contador = 0
while contador <= 8:
    print (f"O contador está com o valor {contador}")
    contador += 1
    
while True:
    numero = int(input("\nDigite um número par: \n"))
    if numero % 2 == 0:
        print ("Você  digitou um número par. Arrasouu!")
    else:
        print ("Você digitou um número ímpar, tente novamente!")
    
    if numero >= 10:
        break
print("Acabou-se o que era doce!") #Esse só vai aparecer quando a condição do while terminar pq ta fora do while

#Listas
numeros = [5, 8, 2, 9, 0, 1, 3, 4]
for numero in numeros:
    if numero % 2 != 0: 
        continue
    print (f"O numero {numero} é par") #Printa só os números pares
    
#Dicionários
dados = {"\nnome": "Lan Code", "inscritos":5000, "categoria":"programação\n"}

for c, v in dados.items(): #Pra cada chave e valor nos items no dicionário ele vai executar o loop, quando usa um dicionário tem que usar o .items
    print(f"{c}: {v}")
    
#Aqui só vai pegar os valores
dados = {"nome": "Lan Code", "inscritos":5000, "categoria":"programação\n"}

for v in dados.values(): #Pra cada chave e valor nos items no dicionário ele vai executar o loop, quando o usa o .values ele vai pegar só os valores
    print(f"{v}")
   
#Aqui vai pegar só as chaves 
dados = {"nome": "Lan Code", "inscritos":5000, "categoria":"programação\n"}

for c in dados.keys(): #Pra cada chave e valor nos items no dicionário ele vai executar o loop, quando o usa o .keys vai pegar só os valores
    print(f"{c}")

#EXERCÍCIOS
#Exercício 1
print("\nExercício 1: Números de 1 a 10 com while")
numero = 1
while numero <= 10:
    print (f"Numero: {numero}")
    numero += 1

#Exercício 2
print("\nExercício 2: Simulador de tabuada")
contador = 0
while contador <= 10:
    numero_user = int(input("Digite um número: "))

    for numero in range(1, 11):
        print (f"{numero_user} x {numero} = {numero_user * numero}")
         
    contador += 1
    if contador >= 10:
        break
print("Te espero na próxima")
       
#Exercício 3
print("\nExercício 3: Quantidade de vogais")
nome = "Giovana"

for vogais in nome:
    if vogais.lower() in ['a', 'e', 'i', 'o', 'u']:
        print(vogais)

#Exercício 4
print("\nExercício 4: Tabuada de 1 a 100")
numero = 1
for n in range(1, 101): 
    print (f"{numero} X {n} = {numero * n}")