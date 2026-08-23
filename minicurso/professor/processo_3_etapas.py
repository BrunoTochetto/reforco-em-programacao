# -*- coding: utf-8 -*-
# =====================================================================
# LAB DE DECURAÇÃO - DESAFIO 1: O PROCESSO DE 3 ETAPAS
# Curso de Informática para Internet (Ensino Médio Técnico)
# Baseado nas metodologias do Computer Science Wiki & MIT
# =====================================================================

"""
TEORIA: O PROCESSO DE 3 ETAPAS DA DEPURACÃO
1. REPRODUZIR (Reproduce): Criar um caso de teste estável e mínimo que force o bug a aparecer.
2. ISOLAR (Isolate): Encontrar o ponto exato ("causa raiz") onde o estado fica corrompido,
   separando o código que funciona do código que quebra usando o breakpoint().
3. CORRIGIR (Fix): Alterar o código para sanar a causa raiz e testar para garantir
   que não quebrou outras funcionalidades (teste de regressão).
"""

import sys

# =====================================================================
# CÓDIGO COM BUG (VERSÃO ERRADA)
# =====================================================================
def sanitizar_e_validar_telefone_errado(telefone_cru):
    """
    Objetivo: Limpar um número de telefone vindo de um formulário web,
    remover espaços, traços e parênteses, e validar se tem exatamente 11 dígitos.
    """
    # Remove caracteres comuns de formatação web
    caracteres_remover = ["(", ")", "-", " "]
    telefone_limpo = telefone_cru
    
    for char in caracteres_remover:
        # BUG: strings em Python são IMUTÁVEIS!
        # telefone_limpo.replace(char, "") gera uma nova string, mas não altera a original.
        # O programador esqueceu de reatribuir: telefone_limpo = telefone_limpo.replace(char, "")
        telefone_limpo.replace(char, "")
    
    # Validação do tamanho
    if len(telefone_limpo) == 11:
        return True
    return False


# =====================================================================
# CÓDIGO CORRIGIDO (VERSÃO CERTA)
# =====================================================================
def sanitizar_e_validar_telefone_certo(telefone_cru):
    """
    Versão corrigida após o isolamento do bug na Etapa 2.
    """
    caracteres_remover = ["(", ")", "-", " "]
    telefone_limpo = telefone_cru
    
    for char in caracteres_remover:
        # CORREÇÃO: Reatribuindo o resultado da substituição
        telefone_limpo = telefone_limpo.replace(char, "")
        
    if len(telefone_limpo) == 11:
        return True
    return False


# =====================================================================
# ÁREA DE TESTES E DEPURACÃO (Para os Alunos executarem)
# =====================================================================
if __name__ == "__main__":
    print("-" * 60)
    print("ETAPA 1: REPRODUZIR O BUG")
    print("-" * 60)
    
    # Caso de teste que reproduz o bug de forma consistente:
    entrada_usuario = "(11) 99999-1234" 
    print(f"Entrada recebida da Web: '{entrada_usuario}'")
    
    # Com os caracteres removidos, o resultado deveria ser "11999991234" (11 dígitos -> Válido)
    resultado_errado = sanitizar_e_validar_telefone_errado(entrada_usuario)
    print(f"Resultado com Bug: {resultado_errado} (Esperado: True)")
    
    print("\n" + "-" * 60)
    print("ETAPA 2: ISOLAR O BUG (INSTRUÇÕES)")
    print("-" * 60)
    print("Alunos: Para isolar, descomentem a linha com 'breakpoint()' abaixo,")
    print("rode o script e inspecione a variável 'telefone_limpo' a cada passo.")
    print("Use o comando 'n' (next) para andar e 'p telefone_limpo' para ver o valor.")
    
    # breakpoint() # <-- DESCOMENTE AQUI PARA DEPURAR!
    
    print("\n" + "-" * 60)
    print("ETAPA 3: TESTE DE REGRESSÃO DA CORREÇÃO")
    print("-" * 60)
    resultado_certo = sanitizar_e_validar_telefone_certo(entrada_usuario)
    print(f"Resultado Corrigido: {resultado_certo} (Esperado: True)")
    
    # Teste de regressão (garantir que um caso simples sem formatação continua funcionando)
    caso_simples = "11999991234"
    print(f"Teste de Regressão com '{caso_simples}': {sanitizar_e_validar_telefone_certo(caso_simples)} (Esperado: True)")
    print("-" * 60)
