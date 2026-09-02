# -*- coding: utf-8 -*-
"""
RESOLUÇÃO DO CADERNO DE EXERCÍCIOS: LISTAS E COLEÇÕES MUTÁVEIS
Componente Curricular: Programação I
Professor: Alisson Zanetti
Estudante Gabarito
"""

print("="*80)
print("RESOLUÇÃO DO CADERNO DE EXERCÍCIOS: LISTAS")
print("="*80)

# --- Questão 1: Mutabilidade e Fatiamento de Listas ---
print("\n[Questão 1] Modificação e Erros de Índices:")
numeros = [10, 20, 30, 40, 50, 60]
print("Original:", numeros)

# a) Alterar primeiro elemento para 15 e o último para 99
numeros[0] = 15
numeros[-1] = 99
print("Após item (a):", numeros)

# b) Substituir os intermediários [30, 40] (índices 2 e 3) por [100, 200] usando fatiamento
# Note que na lista modificada na etapa 'a', os elementos nos índices 2 e 3 ainda são 30 e 40
numeros[2:4] = [100, 200]
print("Após item (b):", numeros)

# c) Executar print(numeros[6]) gera o erro:
# IndexError: list index out of range.
# Justificativa: A lista numeros contém exatamente 6 elementos (índices de 0 a 5). 
# Tentar acessar o índice 6 busca uma posição inexistente além dos limites da lista.


# --- Questão 2: Remoção Progressiva de Elementos ---
print("\n[Questão 2] Remoção de Elementos:")
valores = ['a', 'b', 'c', 'd', 'e', 'f']
print("Lista Inicial:", valores)

# 1. del valores[1] -> remove o elemento 'b' (índice 1)
del valores[1]
print("Após 'del valores[1]':", valores)  # ['a', 'c', 'd', 'e', 'f']

# 2. del valores[2:4] -> remove os índices 2 e 3 da lista atualizada (elementos 'd' e 'e')
# Note que na lista ['a', 'c', 'd', 'e', 'f'], o índice 2 é 'd' e o índice 3 é 'e'.
del valores[2:4]
print("Após 'del valores[2:4]':", valores)  # ['a', 'c', 'f']

# 3. valores.remove('f') -> procura e remove o valor 'f'
valores.remove('f')
print("Após 'valores.remove(\'f\')':", valores)  # ['a', 'c']


# --- Questão 3: Função analisar_notas_classe(lista_notas) ---
print("\n[Questão 3] Função analisar_notas_classe() (Sem usar append):")
def analisar_notas_classe(lista_notas):
    """
    Ordena e analisa notas da classe sem alterar a lista enviada.
    """
    # a) Criação de clone seguro para evitar apelidamento
    clone = lista_notas[:]
    
    # b) Ordenação em ordem crescente
    clone.sort()
    
    # c) Encontrar menor e maior nota
    menor = clone[0]
    maior = clone[-1]
    
    # d) Média aritmética simples
    soma = sum(clone)
    media = soma / len(clone)
    
    print(f"Lista de Notas (Clonada e Ordenada): {clone}")
    print(f"Menor Nota: {menor} | Maior Nota: {maior}")
    return media

notas_turma = [8.5, 6.0, 7.0, 9.5, 5.0]
media_final = analisar_notas_classe(notas_turma)
print(f"Média Final Retornada: {media_final:.2f}")
print(f"Lista de Notas Original (Preservada): {notas_turma}")


# --- Questão 4: Apelidamento (Aliasing) e Clonagem ---
print("\n[Questão 4] Apelidamento e Clonagem:")
# a) A saída será [99, 2, 3].
# Explicação: O comando 'lista_b = lista_a' faz com que ambas as variáveis apontem para 
# o mesmo objeto de lista na memória (apelidamento). Como listas são mutáveis, qualquer 
# modificação por meio de 'lista_b' altera o único objeto existente, afetando também 'lista_a'.

# b) Solução corrigida com fatiamento ou cópia:
lista_a = [1, 2, 3]
lista_b = lista_a[:]  # ou lista_b = lista_a.copy()
lista_b[0] = 99
print("Original lista_a:", lista_a)
print("Modificada lista_b:", lista_b)


# --- Questão 5: Passagem de Parâmetros por Referência ---
print("\n[Questão 5] Passagem de Parâmetros por Referência:")
# Se executarmos:
# meus_dados = [2, 4, 6]
# duplicar_elementos(meus_dados)
# O conteúdo da variável meus_dados será permanentemente alterado para [4, 8, 12].
# Justificativa: Tipos compostos como listas são passados para funções por referência. 
# A variável 'vetor' na função aponta para o mesmo objeto que 'meus_dados' no escopo principal. 
# Como as alterações de indexação 'vetor[i] = ...' são executadas diretamente sobre esse objeto mutável, 
# as modificações persistem mesmo após a finalização da função.

def duplicar_elementos(vetor):
    for i in range(len(vetor)):
        vetor[i] = vetor[i] * 2

meus_dados = [2, 4, 6]
print("Antes da função:", meus_dados)
duplicar_elementos(meus_dados)
print("Depois da função:", meus_dados)


# --- Questão 6: Função gerenciar_estoque(produtos) ---
print("\n[Questão 6] Função gerenciar_estoque():")
def gerenciar_estoque(produtos):
    """
    Executa contagem, busca de índice e ordenação reversa.
    """
    # 1. Contar ocorrências do produto "Teclado"
    contagem_teclado = produtos.count("Teclado")
    
    # 2. Identificar o primeiro índice do produto "Mouse"
    # Tratamos o erro caso 'Mouse' não esteja na lista para segurança do código
    if "Mouse" in produtos:
        indice_mouse = produtos.index("Mouse")
    else:
        indice_mouse = -1
        
    # 3. Ordenar a lista em ordem alfabética reversa de forma in-place
    produtos.sort(reverse=True)
    
    print(f"Quantidade de Teclados: {contagem_teclado}")
    print(f"Primeiro índice do Mouse: {indice_mouse}")
    print(f"Estoque Ordenado Reversamente: {produtos}")
    return indice_mouse

estoque = ["Teclado", "Mouse", "Monitor", "Teclado", "Gabinete"]
print("Estoque Inicial:", estoque)
gerenciar_estoque(estoque)
print("="*80)
