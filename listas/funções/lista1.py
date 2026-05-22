# #########################################################
# # Lista exercício de Funções 1 - Reforço de programação #
# #########################################################

# 1. Faça uma função em que você indique um caracter e um número de caracteres para repetí-lo, exemplo:
# >> repetir("#", 8)
# ########
def repetir(texto, vezes):
    print(texto * vezes)

# 2. Crie uma função em que você pode colocar um texto desejado em um "Letreiro", exemplo: 
# >> letreiro( "Jaser" )
# =========
# = Jaser =
# =========
def letreiro(nome):
    repetir('=', 12)
    print('= ' + nome + ' =')
    repetir('=', 12)

# 2.1 Desafio: Faça em que isso seja dinâmico, tente usar o comando len() para fazer isso.
# >> letreiro("Jaser")         | >>letreiro("Mazzutti")
# =========                        ===============
# = Jaser =                          =  Mazzutti =
# =========                        ===============
def letreiro(nome):
    tamanhoDiv = len(nome) + 4
    repetir('=', tamanhoDiv)
    print('= ' + nome + ' =')
    repetir('=', tamanhoDiv)

# 3. Faça uma função em que você pode colocar alguns textos e deixem eles em 
# * formato 
# * de 
# * itens

# Exemplo:
# >> itens("Sabrina Carpenter", "Billie Eilish", "TV Girl")
# # Sabrina Carpenter
# # Billie Eilish
# # TV Girl
def itens(item1, item2, item3, item4, item5):
    print('#' + item1)
    print('#' + item2)
    print('#' + item3)
    print('#' + item4)
    print('#' + item5)

# 4. Faça um rodapé "customizado" para uma aplicação, ele terá uma linha horizontal de um tamanho e que tenha um texto abaixo.
# Tente fazer com que o texto esteja centralizado. (No arquivo .py faz a formatação ficar estranha, no código é pra ficar certo!)
# exemplo:
# >> tamanhoRodape = 10
# >> rodape("O Fim", tamanhoRodape)
# ================
#      O fim


# >> tamanhoRodape = 15
# >> rodape("Sopa's café", tamanhoRodape)
# ======================
#       Sopa's café

def rodape(texto, tamanhoRodape):
    repetir('=', tamanhoRodape)
    print(' '*(tamanhoRodape//2 - len(texto)//2) + texto)

#Explicação:
# Você tem um tamanho, o do Rodapé, vamos dizer que ele é 10
# Para centralizar algo, você vai precisar do meio dele, então 10 // 2, 
# ==========
#      /\

# Agora você está no meio da barra. E daí vem o texto, se você só colocar o texto, ele vai ir do meio pra frente
# ==========
#      Texto
# Então, você também precisa centralizar o texto. Tamanho do texto dividivo por 2. (tamanho de "Texto" é 5)
# (5 // 2 é 2), e você "junta" os 2. Conta final = tamanhoRodape  // 2 - tamanhoTexto // 2

# ==========
#    Texto
# Centralizado!
# Depois de fazer toda essa conta e raciocínio você pode simplificá-la, fica
# (tamanhoRodape - tamanhoTexto) // 2

# IMPORTANTE LEMBRAR!!
# Não pode ser divisão comum, apenas inteira. A multiplicação de Strings só funciona em INT.




# 5. Faça um programa que reúna todas as funções anteriores e forme uma lista sua e apenas sua!
# Use uma variável para deixar tudo de um mesmo tamanho, customize e deixe como você quiser! Um exemplo de uma lista com os exemplos acima

# miniRepertorio("Bruno", "Reforço", "de", "Programação", "3G"', "Terceiro.")


# ====================
# =       Bruno      =
# ====================
# # Reforço
# # de
# # Programação
# # 3G
# ====================
#       Terceiro


# Customize e faça o que você quiser com isso, mude as funções acima. 
# Tente fazer com que o tamanho do letreiro seja o mesmo que o do rodapé e fique tudo bonitinho.

def miniRepertorio(nome, item1, item2, item3, item4, texto, tamanhoRodape):
    letreiro(nome)
    itens(item1, item2, item3, item4)
    rodape(texto, tamanhoRodape)