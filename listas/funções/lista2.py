#########################################################
# Lista exercício de Funções 2 - Reforço de programação #
#########################################################

# 1) Descreva o que cada linha do código faz.
######################################################

# genero = input("Gênero: ")
# peso = 0
# if genero == "masculino":
#     peso = int(input("Peso total: "))
#     peso = peso * 1.5
# elif genero == "feminino":
#     peso = int(input("Peso total: "))
#     peso = peso * 1.8
                                                 
# altura = float(input("Digite a altura: "))     
# if altura > 100:                               
#     altura = altura / 100                      
# if altura > 1.9:                               
#     peso = peso / 2                            
# elif altura < 1.9:                             
#     peso = peso * 1                            
# print(f" {genero}, {peso}, {altura} ")         

######################################################

# 2) Execute o código (mentalmente, de preferência) com os seguinte dados e o print final:
# 1.Gênero = "feminino"; peso = 50; altura = 191
R = "feminina; 45; 1.91"

# 2.Gênero = "masculino"; peso = 40; altura = 180
R = "masculino; 60; 1.8"

# 3.Gênero = "não informar"; peso = 80; altura = 1.8
R = "não informar; 0; 1.8"

# 2.1) Explique por que na execução do item 2 e 3, eles executaram igualmente mesmo com uma diferença de
# 100x no valor?




# 2.2) O que aconteceria se a altura fosse 190 no item 1.




# 3) Melhore o código.
# Faça ele não ter falhas óbvias. Melhorar o posicionamento de certos comandos, ou excluir comandos... Obviamente, verifique se os resultados são iguais.
# Não existe código errado, o importante é ter os mesmos resultados.
# Qualquer dúvida ou se quiser validar a resolução, venha até o reforço.

genero = input("Gênero: ")
peso = int(input("Peso total: "))
if genero == "masculino":
    peso = peso * 1.5
elif genero == "feminino":
    peso = peso * 1.8
else:
    print("Gênero não reconhecido... Continuando código")
                                                 
altura = float(input("Digite a altura: "))     
if altura > 100:                               
    altura = altura / 100

if altura > 1.9:                               
    peso = peso / 2                            

print(f" {genero}, {peso}, {altura} ")    






