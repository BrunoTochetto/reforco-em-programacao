# =====================================================================
# MINICURSO DE DEPURACAO - DESAFIOS PRATICOS
# Minicurso de Informática para Internet - IFC Concórdia
# Semana de Ensino Pesquisa e Extensão (SEPE)
# =====================================================================

# ---------------------------------------------------------------------
# DESAFIO 3: "O Validador de Usuarios Silencioso"
# Sintoma: Um validador de cadastros para sistemas web que parece funcionar
# perfeitamente, mas se comporta de forma inesperada ou falha silenciosamente
# sob certas combinações de strings.
# ---------------------------------------------------------------------

def validar_dados_cadastro(email, senha):
    """
    Valida se o email possui arroba (@) antes do dominio (.com ou .org)
    e se a senha possui o tamanho minimo de 8 caracteres.
    Retorna True se valido, ou False se invalido.
    """
    
    if len(senha) < 8:
        return False
        
    if "@" not in email or (".com" not in email and ".org" not in email):
        return False
        
    return True


# Codigo de teste:
cadastro1 = validar_dados_cadastro("aluno@escola.com", "senha123")
print("Cadastro 1:", cadastro1)
print("Resultado esperado: True, email certo e senha certa")

cadastro2 = validar_dados_cadastro("escola.com@aluno", "12345678")
print("Cadastro 2:", cadastro2)
print("Resultado esperado: False, email errado e senha certa")

cadastro3 = validar_dados_cadastro("escola@aluno.com", "1234567")
print("Cadastro 2:", cadastro3)
print("Resultado esperado: False, email certo e senha errada")