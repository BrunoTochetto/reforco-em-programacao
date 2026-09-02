# -*- coding: utf-8 -*-
"""
RESOLUÇÃO COMPLETA — CADERNO DE ATIVIDADES DE PROGRAMAÇÃO I (V2)
Componente Curricular: Programação I e Lógica de Computadores
Instituto Federal Catarinense - Campus Concórdia
Professor: Alisson Zanetti

Este arquivo contém o gabarito oficial completo e funcional de todos os exercícios
dos dois cadernos de atividades desenvolvidos para o 1º Ano do Ensino Médio Integrado:
1. Caderno de Atividades Práticas (Tópicos: Strings, Listas, Laços e Funções)
2. Caderno de Análise Lógica (Mapeamento de Fluxogramas para Código Python)

O código foi projetado de forma didática, com comentários explicativos em todas as linhas,
perfeito para visualização e aprendizado dos estudantes.
"""

# =============================================================================
# PARTE I: GABARITO DO CADERNO DE ATIVIDADES PRÁTICAS (TÓPICOS)
# =============================================================================

# --- Exercício S-1 (Física) ---
def limpa_dados_velocidade(velocidade_bruta):
    """
    Remove espaços extras, converte para float e formata com duas casas decimais.
    """
    # 1. Limpa espaços extras no início e fim usando .strip()
    string_limpa = velocidade_bruta.strip()
    
    # 2. Converte para float para possibilitar cálculos
    valor_float = float(string_limpa)
    
    # 3. Retorna a f-string formatada com exatas 2 casas decimais (.2f)
    return f"Velocidade Limpa: {valor_float:.2f} m/s"


# --- Exercício S-2 (Biologia) ---
def analisa_dna(sequencia_bruta):
    """
    Análise biológica de strings de DNA (comprimento, fatiamento de códons e contagem).
    """
    # 1. Limpar espaços e padronizar para letras maiúsculas
    cadeia = sequencia_bruta.strip().upper()
    
    # 2. Obter tamanho da fita
    comprimento = len(cadeia)
    
    # 3. Obter primeiro códon (índices 0 a 2) e último códon (índices -3 a -1)
    primeiro_codon = cadeia[:3]
    ultimo_codon = cadeia[-3:] # uso de índices negativos (fatiamento de trás para frente)
    
    # 4. Contar ocorrências da base nitrogenada Adenina ('A')
    total_A = cadeia.count('A')
    
    # Exibe informações na tela (didático)
    print(f"--- Relatório de DNA: {cadeia} ---")
    print(f"Comprimento da cadeia: {comprimento} bases")
    print(f"Códons Extremos: Inicial={primeiro_codon} | Final={ultimo_codon}")
    print(f"Contagem de Adenina (A): {total_A} bases")
    
    return [cadeia, comprimento, primeiro_codon, ultimo_codon, total_A]


# --- Exercício S-3 (Geografia) ---
def processa_camadas_terra(camadas_raw):
    """
    Separa a string delimitada por '#' e reconstrói com uma seta indicadora.
    """
    # 1. Split quebra a string original em uma lista de elementos usando '#' como divisor
    lista_camadas = camadas_raw.split('#')
    
    # 2. Join junta a lista novamente em uma string, inserindo ' -> ' entre cada elemento
    string_formatada = " -> ".join(lista_camadas)
    
    # Explicação didática de memória:
    # A string reconstruída NÃO é idêntica na memória à original porque strings são objetos IMUTÁVEIS.
    # Qualquer modificação resulta em um novo endereço de objeto ID na memória do Python.
    return string_formatada


# --- Exercício L-1 (Matemática) ---
def analisa_notas(lista_notas):
    """
    Analisa notas de matemática sem alterar a lista original (usando clonagem).
    """
    # Clonagem segura da lista usando o operador de fatia total [:] para preservar a lista original
    copia_notas = lista_notas[:]
    
    # 1. Ordenação in-place da lista clonada
    copia_notas.sort()
    
    # 2. Encontrar notas extremas usando indexação
    menor = copia_notas[0]      # Primeiro elemento (menor)
    maior = copia_notas[-1]     # Último elemento (maior)
    
    # 3. Calcular a média aritmética simples
    soma_total = sum(copia_notas)
    media = soma_total / len(copia_notas)
    
    # 4. Verificar se a nota 7.0 está na lista usando o operador de pertencimento 'in'
    tem_sete = 7.0 in copia_notas
    
    return [copia_notas, menor, maior, round(media, 2), tem_sete]


# --- Exercício L-2 (Educação Financeira) ---
def aplica_desconto_referencia(lista_gastos):
    """
    Aplica 10% de desconto alterando a lista original na memória (Passagem por Referência).
    """
    # Como as listas são mutáveis, as alterações ocorrem no objeto compartilhado
    for i in range(len(lista_gastos)):
        lista_gastos[i] = round(lista_gastos[i] * 0.90, 2)

def aplica_desconto_copia(lista_gastos):
    """
    Aplica 10% de desconto em um clone e retorna o clone (Preserva o original).
    """
    # Criamos uma cópia independente usando o método .copy() ou fatiamento [:]
    lista_clonada = lista_gastos.copy()
    for i in range(len(lista_clonada)):
        lista_clonada[i] = round(lista_clonada[i] * 0.90, 2)
    return lista_clonada


# --- Exercício R-1 (Química) ---
def simular_decaimento_radioativo(massa_inicial):
    """
    Simula decaimento de massa radioativa reduzindo em 50% por minuto até atingir limite.
    """
    massa = massa_inicial
    tempo = 0
    print("\n--- Tabela de Decaimento Radioativo ---")
    print(f"Minuto {tempo:02d} | Massa: {massa:.4f} g")
    
    # O laço roda enquanto a massa for maior ou igual ao limite de estabilidade de 0.05g
    while massa >= 0.05:
        massa = massa / 2
        tempo = tempo + 1
        print(f"Minuto {tempo:02d} | Massa: {massa:.4f} g")
        
    print(f"Estabilidade atingida após {tempo} minutos.")
    return tempo, massa


# --- Exercício R-2 (Artes/Geometria) ---
def gera_escada_numerica(linhas):
    """
    Gera uma escada de números usando laços aninhados (for loops).
    """
    print(f"\n--- Escada Geométrica ({linhas} linhas) ---")
    # O laço externo controla as linhas
    for i in range(1, linhas + 1):
        # O laço interno controla quais números são impressos naquela linha
        for j in range(1, i + 1):
            print(j, end=" ") # end=" " suprime a quebra de linha padrão do Python
        print() # imprime uma linha em branco para quebrar após o término da linha da escada


# --- Exercício F-1 (Educação Financeira) ---
def calcula_juros_compostos(C, i, t):
    """
    Função frutífera pura (usa return) para calcular montante acumulado.
    Fórmula: M = C * (1 + i)^t
    """
    montante = C * ((1 + i) ** t)
    return montante


# --- Exercício F-2 (Matemática Pura) ---
def soma_digitos_recursiva(n):
    """
    Função recursiva para calcular a soma de dígitos de um número positivo.
    """
    # 1. Caso Base: Se o número tiver apenas um dígito (menor que 10), retorne o próprio número
    if n < 10:
        return n
    # 2. Caso Recursivo: Soma o último dígito (n % 10) à soma dos demais dígitos restantes (n // 10)
    else:
        ultimo_digito = n % 10
        demais_digitos = n // 10
        return ultimo_digito + soma_digitos_recursiva(demais_digitos)


# =============================================================================
# PARTE II: GABARITO DO CADERNO DE ANÁLISE LÓGICA (FLUXOGRAMAS)
# =============================================================================

# --- Código do Fluxograma 1: Transporte Escolar ---
def verifica_transporte_escolar(distancia, renda_per_capita):
    """
    Implementação literal do Fluxograma 1.
    Condição: Distância > 15 km OU Renda Per Capita < 1.5 salários mínimos.
    """
    if distancia > 15 or renda_per_capita < 1.5:
        resultado = "Desconto Concedido!"
    else:
        resultado = "Sem Desconto"
    return resultado


# --- Código do Fluxograma 2: Rendimento Escolar ---
def calcula_rendimento_trimestral(n1, n2, n3):
    """
    Implementação literal do Fluxograma 2.
    Se Média >= 7.0: Aprovado.
    Se Média < 4.0: Reprovado.
    Caso contrário: Recuperação.
    """
    media = (n1 + n2 + n3) / 3
    
    if media >= 7.0:
        situacao = "Aprovado!"
    else:
        # Desvio encadeado
        if media < 4.0:
            situacao = "Reprovado!"
        else:
            situacao = "Recuperação!"
            
    return media, situacao


# --- Código do Fluxograma 3: Crescimento Bacteriano ---
def simula_crescimento_bacteriano(P, L):
    """
    Implementação literal do Fluxograma 3.
    Dobra a população bacteriana P a cada ciclo (tempo t) enquanto P < L.
    """
    t = 0
    while P < L:
        P = P * 2
        t = t + 1
    return t


# --- Código do Fluxograma 4: Validação de Entrada de Dados ---
def valida_entrada_par_positivo(numero_digitado):
    """
    Implementação do Fluxograma 4 como uma verificação individual.
    Em um ambiente real, rodaria dentro de um laço interativo (encontrado nos testes abaixo).
    """
    if numero_digitado > 0 and numero_digitado % 2 == 0:
        return "Valor aceito!"
    else:
        return "Número inválido, tente novamente."

