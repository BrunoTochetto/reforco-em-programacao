# -*- coding: utf-8 -*-
"""
RESOLUÇÃO DO CADERNO DE EXERCÍCIOS: STRINGS E MANIPULAÇÃO DE TEXTO
Componente Curricular: Programação I
Professor: Alisson Zanetti
Estudante Gabarito
"""

print("="*80)
print("RESOLUÇÃO DO CADERNO DE EXERCÍCIOS: STRINGS")
print("="*80)

# --- Questão 1: Imutabilidade e Erro de Tipo (TypeError) ---
print("\n[Questão 1] Erro de Imutabilidade:")
# Explicação: Strings em Python são imutáveis. Tentar atribuir um valor a um índice 
# como 'saudacao[0] = "A"' gera o erro 'TypeError: "str" object does not support item assignment'.
# A forma correta é concatenar o caractere desejado com o restante da string usando fatiamento.

saudacao = "alô, mundo!"
saudacao_correta = 'A' + saudacao[1:]
print("Original:", saudacao)
print("Corrigido:", saudacao_correta)


# --- Questão 2: Fatiamento (Slicing) de Strings ---
print("\n[Questão 2] Fatiamento de 'Programação em Python':")
texto = "Programação em Python"

# a) Apenas os 11 primeiros caracteres ("Programação")
parte_a = texto[:11]  # ou texto[0:11]
# b) Apenas a palavra final da frase ("Python")
parte_b = texto[15:]  # ou texto[15:21]
# c) O último caractere da string usando índice negativo
parte_c = texto[-1]

print("a) Primeiros 11 caracteres:", parte_a)
print("b) Palavra final:", parte_b)
print("c) Último caractere:", parte_c)


# --- Questão 3: Comparação Relacional e Ordem ASCII ---
print("\n[Questão 3] Comparação Relacional de 'Zebra' e 'banana':")
# Explicação: No padrão ASCII/Unicode, todas as letras maiúsculas vêm antes das minúsculas 
# ('A'-'Z' são 65-90; 'a'-'z' são 97-122). Como 'Z' (90) é menor que 'b' (98), 
# a expressão 'palavra1 < palavra2' avalia para True. Portanto, "Zebra" vem antes de "banana".

palavra1 = "Zebra"
palavra2 = "banana"
if palavra1 < palavra2:
    print(f"'{palavra1}' vem antes de '{palavra2}' na ordem alfabética.")
else:
    print(f"'{palavra2}' vem antes de '{palavra1}' na ordem alfabética.")


# --- Questão 4: Função analisar_ocorrencias(texto, sub) ---
print("\n[Questão 4] Função analisar_ocorrencias():")
def analisar_ocorrencias(texto, sub):
    """
    Conta e descobre a primeira ocorrência de uma substring em um texto.
    """
    contagem = texto.count(sub)
    primeiro_indice = texto.find(sub)
    
    if primeiro_indice == -1:
        return f"A substring '{sub}' não foi encontrada no texto."
    else:
        return f"A substring '{sub}' ocorre {contagem} vez(es). Primeira ocorrência no índice: {primeiro_indice}."

# Teste prático
frase_teste = "banana"
sub_teste = "na"
print(analisar_ocorrencias(frase_teste, sub_teste))


# --- Questão 5: Função formatar_nome_usuario(nome_bruto) ---
print("\n[Questão 5] Função formatar_nome_usuario():")
def formatar_nome_usuario(nome_bruto):
    """
    Limpa espaços excessivos, converte para maiúsculo e retorna string formatada.
    """
    nome_limpo = nome_bruto.strip()
    nome_maiusculo = nome_limpo.upper()
    comprimento = len(nome_maiusculo)
    return f"Usuário: {nome_maiusculo} (Comprimento: {comprimento} caracteres)"

# Teste prático
print(formatar_nome_usuario("   João da Silva   "))


# --- Questão 6: Função reverter_palavras(frase) ---
print("\n[Questão 6] Função reverter_palavras():")
def reverter_palavras(frase):
    """
    Quebra uma frase em palavras, reverte a ordem delas e junta novamente.
    """
    palavras = frase.split()  # Quebra a frase usando espaços em branco como delimitador
    palavras_revertidas = palavras[::-1]  # Reverte a lista de palavras usando fatiamento
    frase_revertida = " ".join(palavras_revertidas)  # Une a lista de volta em uma string
    return frase_revertida

# Teste prático
frase_original = "A persistência realiza o impossível"
print("Original:", frase_original)
print("Revertida:", reverter_palavras(frase_original))
print("="*80)
