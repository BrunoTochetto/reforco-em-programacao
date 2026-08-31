
# =====================================================================
# Minicurso de Informática para Internet - IFC Concórdia
# Semana de Ensino Pesquisa e Extensão (SEPE)
# Baseado nas metodologias do Computer Science Wiki & MIT
# =====================================================================

"""
TEORIA: O PROCESSO DE 3 ETAPAS DA DEPURACÃO
1. REPRODUZIR: Criar um caso de teste estável e mínimo que force o bug a aparecer.
2. ISOLAR: Encontrar o ponto exato ("causa raiz") onde o estado fica corrompido,
   separando o código que funciona do código que quebra usando o breakpoint().
3. CORRIGIR: Alterar o código para sanar a causa raiz e testar para garantir
   que não quebrou outras funcionalidades (teste de regressão).
"""

import sys

# =====================================================================
# CÓDIGO COM BUG
# =====================================================================
def sanitizar_e_validar_telefone_original(telefone_cru):
    """
    Objetivo: Limpar um número de telefone vindo de um formulário web,
    remover espaços, traços e parênteses, e validar se tem exatamente 11 dígitos.
    """
    # Remove caracteres comuns de formatação web
    caracteres_remover = ["(", ")", "-", " "]
    telefone_limpo = telefone_cru
    
    for char in caracteres_remover:
        telefone_limpo.replace(char, "")
    
    # Validação do tamanho
    if len(telefone_limpo) == 11:
        return True
    return False


# Com os caracteres removidos, o resultado deveria ser "12123451234" (11 dígitos -> Válido)
entrada1 = "(12) 12345-1234"
print(sanitizar_e_validar_telefone_original(entrada1))
print("Resultado esperado: TRUE")

print("=================================")

# Com os caracteres removidos, o resultado deveria ser "121234561234" (12 dígitos -> Inválido)
entrada2 = "(12) 123456-1234"
print(sanitizar_e_validar_telefone_original(entrada2))
print("Resultado esperado: FALSE")

print("=================================")
# Com os caracteres removidos, o resultado deveria ser "123451234" (10 dígitos -> Inválido)
entrada3 = "12345-1234"
print(sanitizar_e_validar_telefone_original(entrada3))
print("Resultado esperado: FALSE")

print("=================================")
# Com os caracteres removidos, o resultado deveria ser "55123451234" (11 dígitos -> Válido)
entrada4 = "55 123451234"
print(sanitizar_e_validar_telefone_original(entrada4))
print("Resultado esperado: TRUE")