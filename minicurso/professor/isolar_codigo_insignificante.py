# -*- coding: utf-8 -*-
# =====================================================================
# LAB DE DECURAÇÃO - DESAFIO 3: ISOLAR O CÓDIGO MAIS INSIGNIFICANTE
# Curso de Informática para Internet (Ensino Médio Técnico)
# Baseado nas metodologias do computersciencewiki.org (MRE/MWE)
# =====================================================================

"""
TEORIA: ISOLAR O CÓDIGO MAIS INSIGNIFICANTE (MINIMAL REPRODUCIBLE EXAMPLE)
Muitas vezes, um bug acontece em meio a centenas de linhas de código com acessos a bancos de dados,
conexões de rede fictícias, logs e variáveis complexas. Isso gera um ruído que esconde a falha.

A técnica consiste em ir removendo/limpando tudo o que é irrelevante no programa até restar
apenas o menor trecho de código possível (mais "insignificante") que ainda reproduza o bug.
Ao reduzir o código ao seu estado mais básico, a causa raiz torna-se imediatamente visível!
"""

# =====================================================================
# SISTEMA DE LOGIN DE SITE (CÓDIGO INFLADO / COM RUIDO / COM BUG)
# =====================================================================
def tentar_login_no_sistema_errado(user_id_form, senha_form):
    """
    Simula uma requisição web complexa com conexão de banco de dados,
    geração de chaves criptográficas, verificação de IPs, logs de auditoria
    e finalmente a validação do usuário.
    """
    # Ruído 1: Conexão simulada com banco de dados
    banco_dados_usuarios = [
        {"id": 100, "nome": "admin", "senha": "hash_secure_123", "nivel": "total"},
        {"id": 101, "nome": "aluno", "senha": "hash_secure_456", "nivel": "comum"},
        {"id": 102, "nome": "professor", "senha": "hash_secure_789", "nivel": "medio"}
    ]
    
    # Ruído 2: Logs e auditoria de segurança
    print("[LOG SISTEMA] Iniciando handshake de login...")
    print(f"[LOG SEGURANÇA] IP do cliente verificado. Handshake OK para user_id: {user_id_form}")
    
    # Ruído 3: Criação de chaves temporárias para a sessão
    session_token = "SESSION_" + str(user_id_form) + "_XYZ"
    
    # Validação REAL do login (Onde o bug realmente mora)
    usuario_encontrado = None
    for usuario in banco_dados_usuarios:
        # BUG SUTIL DE TIPO (TypeError / Bug Lógico):
        # O formulário web sempre envia os dados como STRING (ex: user_id_form = "101")
        # No banco de dados, o "id" é gravado como INTEIRO (ex: 101)
        # Comparar int com str em Python usando '==' sempre retorna False sem dar erro!
        if usuario["id"] == user_id_form:
            usuario_encontrado = usuario
            break
            
    # Continuação do ruído (geração de logs subsequentes)
    if usuario_encontrado:
        if usuario_encontrado["senha"] == "hash_" + senha_form:
            print("[LOG AUDITORIA] Login concedido e gravado na tabela de acessos.")
            return {"status": "sucesso", "token": session_token}
        else:
            print("[LOG AUDITORIA] Falha de login: senha incorreta.")
            return {"status": "erro", "motivo": "Senha inválida"}
    
    print("[LOG AUDITORIA] Falha de login: usuário não existe no banco de dados.")
    return {"status": "erro", "motivo": "Usuário inexistente"}


# =====================================================================
# CÓDIGO INSIGNIFICANTE ISOLADO (O CÓDIGO MÍNIMO QUE REPRODUZ O ERRO)
# =====================================================================
def isolar_e_reproduzir_bug():
    """
    Aqui nós limpamos TODO o ruído do banco de dados fictício, tokens de sessão e logs.
    Restou apenas a comparação direta que causava a quebra lógica!
    """
    print("\nCÓDIGO INSIGNIFICANTE ISOLADO:")
    id_no_banco = 101       # Tipo: int
    id_no_formulario = "101" # Tipo: str (vindo da web)
    
    # Ao testar apenas esse trecho insignificante, o problema fica óbvio para os alunos:
    print(f"Tipo ID Banco: {type(id_no_banco)}")
    print(f"Tipo ID Form: {type(id_no_formulario)}")
    print(f"Comparando {id_no_banco} == '{id_no_formulario}': {id_no_banco == id_no_formulario}")
    print("Conclusão: Um inteiro nunca será igual a uma string em Python!")


# =====================================================================
# CÓDIGO CORRIGIDO (VERSÃO CERTA)
# =====================================================================
def tentar_login_no_sistema_certo(user_id_form, senha_form):
    """
    Versão corrigida após isolarmos e entendermos que precisávamos converter o tipo do ID.
    """
    banco_dados_usuarios = [
        {"id": 100, "nome": "admin", "senha": "hash_secure_123", "nivel": "total"},
        {"id": 101, "nome": "aluno", "senha": "hash_secure_456", "nivel": "comum"},
        {"id": 102, "nome": "professor", "senha": "hash_secure_789", "nivel": "medio"}
    ]
    
    usuario_encontrado = None
    for usuario in banco_dados_usuarios:
        # CORREÇÃO: Convertemos o dado do formulário web (string) para inteiro antes de comparar!
        # Ou fazemos str(usuario["id"]) == user_id_form
        if usuario["id"] == int(user_id_form):
            usuario_encontrado = usuario
            break
            
    if usuario_encontrado:
        if usuario_encontrado["senha"] == "hash_" + senha_form:
            return {"status": "sucesso", "token": "SESSION_" + str(user_id_form)}
            
    return {"status": "erro", "motivo": "Dados inválidos"}


# =====================================================================
# ÁREA DE EXECUÇÃO
# =====================================================================
if __name__ == "__main__":
    print("-" * 75)
    print("SINTOMA DO BUG NO SISTEMA COMPLEXO:")
    print("-" * 75)
    
    # O Aluno tenta entrar com o ID 101 e a senha secure_456 (usuário existe!)
    resultado = tentar_login_no_sistema_errado("101", "secure_456")
    print(f"Resultado do Login: {resultado}")
    print("Sintoma: O login diz que o usuário não existe, mesmo ele estando no banco!")
    
    # Agora demonstramos o isolamento
    isolar_e_reproduzir_bug()
    
    print("\n" + "-" * 75)
    print("APLICANDO A CORREÇÃO NO SISTEMA")
    print("-" * 75)
    resultado_corrigido = tentar_login_no_sistema_certo("101", "secure_456")
    print(f"Resultado corrigido: {resultado_corrigido}")
    print("-" * 75)
