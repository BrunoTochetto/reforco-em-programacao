# -*- coding: utf-8 -*-
"""
RESOLUÇÃO DO CADERNO DE EXERCÍCIOS: LAÇOS DE REPETIÇÃO
Componente Curricular: Programação I
Professor: Alisson Zanetti
Estudante Gabarito
"""

print("="*80)
print("RESOLUÇÃO DO CADERNO DE EXERCÍCIOS: LAÇOS DE REPETIÇÃO")
print("="*80)

# --- Questão 1: Função exibir_multiplos(n, limite) ---
print("\n[Questão 1] Função exibir_multiplos():")
def exibir_multiplos(n, limite):
    """
    Exibe os múltiplos de n menores ou iguais ao limite na mesma linha.
    """
    i = 1
    while n * i <= limite:
        print(n * i, end="   ")
        i += 1
    print()  # Quebra de linha final

# Teste prático
exibir_multiplos(3, 20)


# --- Questão 2: Sequência Numérica e Mesa de Rastreio ---
print("\n[Questão 2] Sequência e Mesa de Rastreio:")
# Explicação do item a):
# Se n inicial for 3:
# - n é ímpar: n = 3 * 3 + 1 = 10 (imprime 3)
# - n é par: n = 10 / 2 = 5 (imprime 10)
# - n é ímpar: n = 5 * 3 + 1 = 16 (imprime 5)
# - n é par: n = 16 / 2 = 8 (imprime 16)
# - n é par: n = 8 / 2 = 4 (imprime 8)
# - n é par: n = 4 / 2 = 2 (imprime 4)
# - n é par: n = 2 / 2 = 1 (imprime 2)
# - Loop termina porque n se tornou 1. (imprime 1 final)
# Sequência impressa: 3 10 5 16 8 4 2 1

# Explicação do item b):
# Um "loop infinito" ocorre quando a condição do laço de repetição (como 'n != 1') avalia
# sempre para True, impossibilitando a parada da execução. Se a condição de parada nunca 
# fosse alcançada, o computador executaria o laço indeterminadamente até que a memória fosse
# saturada ou o programa fosse forçado a encerrar pelo sistema operacional.

def sequencia(n):
    while n != 1:
        print(int(n), end=" ")
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
    print(1)

print("Sequência para n = 3:")
sequencia(3)


# --- Questão 3: Programa com while True e break ---
print("\n[Questão 3] Programa de Acumulação com Parada (Simulado):")
# Simulação da execução com entradas de teste simuladas [4, 7, 2, 0]:
def simular_programa_acumulador(entradas):
    soma = 0
    indice_leitura = 0
    while True:
        # No terminal real, usaríamos: valor = int(input("Digite um número (0 para sair): "))
        valor = entradas[indice_leitura]
        print(f"Número digitado pelo usuário: {valor}")
        if valor == 0:
            break
        soma += valor
        indice_leitura += 1
    print(f"Laço finalizado. Soma total: {soma}")

simular_programa_acumulador([4, 7, 2, 0])


# --- Questão 4: Função imprimir_indices_pares(lista) ---
print("\n[Questão 4] Função imprimir_indices_pares():")
def imprimir_indices_pares(lista):
    """
    Exibe elementos da lista que estão localizados em índices pares.
    """
    for i in range(len(lista)):
        if i % 2 == 0:
            print(f"Índice {i}: {lista[i]}")

# Teste prático
nomes = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo", "Fernanda"]
imprimir_indices_pares(nomes)


# --- Questão 5: Paralelismo com enumerate() ---
print("\n[Questão 5] Paralelismo de Listas com enumerate():")
vendedores = ['José', 'Marcos', 'Joana', 'Maria']
vendas = [500, 200, 300, 100]

for i, vendedor in enumerate(vendedores):
    print(f"Vendedor {i + 1}: {vendedor} - Vendas: R$ {vendas[i]}")


# --- Questão 6: Função gerar_tabuada_completa() ---
print("\n[Questão 6] Tabuada Completa (Laços Aninhados):")
def gerar_tabuada_completa():
    """
    Imprime as tabuadas de multiplicação de 1 a 10 de forma estruturada.
    """
    for i in range(1, 11):
        print(f"\n--- TABUADA DO {i} ---")
        for j in range(1, 11):
            resultado = i * j
            print(f"{i} x {j:2d} = {resultado:2d}")

# Chamada do teste
gerar_tabuada_completa()
print("="*80)
