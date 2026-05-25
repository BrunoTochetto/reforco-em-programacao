# #########################################################
# # Lista exercício de Funções 3 - Reforço de programação #
# #########################################################

### Dado o código:

#########################################################################
faltas = int(input(“Faltas: “)),
maximoFaltas = int(input(“Máximo de faltas: ”))

mensagem = "Tudo certo!"
if faltas > maximoFaltas:
    mensagem = "Reprovado por faltas."

if faltas == maximoFaltas:
    mensagem = "Não poderá faltar mais."
print(mensagem)


faltas = int(input(“Faltas: “))
maximoFaltas = int(input(“Máximo de faltas: ”))

mensagem = "Tudo certo!"
if faltas > maximoFaltas:
    mensagem = "Reprovado por faltas."
    
if faltas == maximoFaltas:
    mensagem = "Não poderá faltar mais."
print(mensagem)

faltas = int(input(“Faltas: “))
maximoFaltas = int(input(“Máximo de faltas: ”))

mensagem = "Tudo certo!"
if faltas > maximoFaltas:
    mensagem = "Reprovado por faltas."
    
if faltas == maximoFaltas:
    mensagem = "Não poderá faltar mais."
print(mensagem)

faltas = int(input(“Faltas: “))
maximoFaltas = int(input(“Máximo de faltas: ”))

mensagem = "Tudo certo!"
if faltas > maximoFaltas:
    mensagem = "Reprovado por faltas."
    
if faltas == maximoFaltas:
    mensagem = "Não poderá faltar mais."
print(mensagem)

faltas = int(input(“Faltas: “))
maximoFaltas = int(input(“Máximo de faltas: ”))

mensagem = "Tudo certo!"
if faltas > maximoFaltas:
    mensagem = "Reprovado por faltas."
    
if faltas == maximoFaltas:
    mensagem = "Não poderá faltar mais."
print(mensagem)
#########################################################################

# 1) Execute o código (mentalmente, de preferência) e descreva o que ele faz.

aspasResposta = "O importante da resposta é falar que 'é o mesmo código que se repete 4 vezes'."


# 2) O código tem alguns conceitos que poderiam ser aplicados, dado seu conhecimento sobre python, é correto afirmar que: (Justifique as falsas!)
#      1. O código é fácil de entender, sem repetições desnecessárias, assim, um código completo. #
#      2. É um código simples, porém, não é preciso a variável “mensagem” #
#      4. É possível criar uma função para padronizar o código. #
#      8. Poderia existir apenas uma variável “mensagem” no início do código, com as próximas apenas dentro dos IFs. #
#      16. É possível criar uma função para padronizar este código, porém, os inputs ainda devem ficar fora da função. #
#      32. Se for alterado o texto do input de faltas, será preciso apenas alterar o do primeiro input para o código inteiro. #
#      64. É possível transformar o segundo IF em um ELIF ou em ELSE.


Soma = 4

# 3) Reescreva o código em 13 linhas e certifique-se que ele funciona igualmente.
def verificarFaltas():
    faltas = int(input(“Faltas: “)),
    maximoFaltas = int(input(“Máximo de faltas: ”))
    mensagem = "Tudo certo!"
    if faltas > maximoFaltas:
        mensagem = "Reprovado por faltas."
    if faltas == maximoFaltas:
        mensagem = "Não poderá faltar mais."
    print(mensagem)
verificarFaltas()
verificarFaltas()
verificarFaltas()
verificarFaltas()
##################################