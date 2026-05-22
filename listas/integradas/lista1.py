#############################################################
# Lista integrada de programação 1 - Reforço de programação #
#############################################################

# 1) Em um mundo cheio de camadas para chegar até o centro da Terra,
# crie um programa que receba um valor em Quilômetros e retorne a camada da terra correspondente.
# 0 km seria a superfície e 6378 km o núcleo.

# Tabela - Camadas da Terra
#######################################
# Crosta continental
# 0 até 70km
# Astenosfera
# 75 km até 650 km
# Mesosfera
# 650 km até 2900 km
# Núcleo externo
# 2900 km até 5150 km
# Núcleo interno
# 5150 km até 6378 km
#######################################
# Exemplos: 
# Entradas: quilometros  = 71 km                            Saída: Astenosfera.
# Entradas: quilmetros   = 6010 km                          Saída: Núcleo interno.
# Entradas: quilometros  = 1250 km                          Saída: Mesosfera.

# 2) Na física o Movimento Retilíneo Uniforme (MRU) é o movimento que ocorre com velocidade constante em uma trajetória reta.
# Desta forma, em intervalos de tempos iguais o móvel percorre a mesma distância. Fórmula:

# Vm = deltaS / deltaT

# Porém, em um certo experimento, a velocidade média já foi calculada, mas não se sabe ao certo a distância percorrida.
# Faça uma função em que receba: a velocidade média e o tempo, retornando a distância percorrida no experimento.

# Exemplos: 
# Entradas: velocidadeMedia = 20; tempo = 2;       Saída: 40 metros.
# Entradas: velocidadeMedia = 2.5; tempo = 50;    Saída: 125 metros.
# Entradas: velocidadeMedia = 37.5; tempo = 3.5; Saída: 131.25 metros.

# 3) Faça uma função que receba continuamente um valor de: Citosina, Guanina, Timina ou Adenosina (DNA) e retorne seu respectivo par de bases nitrogenadas.
# E acabe a função quando o usuário digitar zero, retornando a sequência final.

# RNA: Citosina, Guanina, Adenina, Uracila.            | C + G   e   A + U
# DNA: Citosina, Guanina, Adenina, Timina              | C + G   e   A + T

# Desafio adicional: Faça com que a função detecte automáticamente se é um DNA ou RNA que o usuário está digitando. E no retorno se é um DNA ou RNA.

# Exemplos:
# Entradas: C G A A A U G A 0                         Saída: RNA; C-G G-C A-U A-U A-U U-A G-C A-U
# Entradas: C G T A A T G A 0                         Saída: DNA; C-G G-C T-A A-T A-T T-A G-C A-T



