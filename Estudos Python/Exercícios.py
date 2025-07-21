nome = str("Giovana")
idade = int(17)
nota_final = float(9.99)
aprovado = bool(True)

print (f"Olá meu nome é {nome}, tenho {idade} anos,  minha nota é {nota_final} e eu fui aprovado: {aprovado}")

var_int = "25"
var_int_convert = 25
var_float = 9.8
var_float_convert = "9.8"

print(type(var_int))
print(type(var_int_convert))
print(type(var_float))
print(type(var_float_convert))

nome_completo = "Giovana Cristina Brito Pereira"
quantidade_letras = len(nome_completo.replace(" ", ""))
print (nome_completo.split()[0])
print (nome_completo.upper())
print (quantidade_letras)

preco_produto = 120
quantidade = 30
desconto = 10
val_total = preco_produto + quantidade - desconto
print ("O valor total é", val_total)