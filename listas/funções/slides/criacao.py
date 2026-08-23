def somarSucessivas(valor1, valor2, valor3, valor4):
    resultado = valor1 + valor2 + valor3 + valor4
    print(resultado)

somarSucessivas(1, 2, 3, 4)
# 10

idade = 12
valores = 10
ifc = 61
horas = 100
somarSucessivas(idade, valores, ifc, horas)
#183

def concatenarStrENumero(string, numero):
    return string + str(numero)

concatenarStrENumero('Alisson', 18)

nome = "Lara"
valor = 17
concatenacao = concatenarStrENumero(nome, valor)

def repetirCaracter(string, quantidade, prefixo='', sufixo=''):
       print(prefixo + string * quantidade + sufixo)
    
repetirCaracter("#=-", 8)
#=-#=-#=-#=-#=-#=-#=-#=-

repetirCaracter("ZX", 4, prefixo="#", sufixo="123")
#ZXZXZXZX123

def printBonito(texto):
    print('===========')
    print(texto)
    print('===========')