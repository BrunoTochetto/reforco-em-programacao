
# =====================================================================
# Minicurso de Informática para Internet - IFC Concórdia
# Semana de Ensino Pesquisa e Extensão (SEPE)
# Baseado nas metodologias do Computer Science Wiki
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
# SISTEMA DE LOGIN DE SITE
# =====================================================================
def tentar_login_no_sistema_original(user_id_form, senha_form):
    """
    Simula uma requisição web complexa com conexão de banco de dados,
    geração de chaves criptográficas, verificação de IPs, logs de auditoria
    e finalmente a validação do usuário.
    """
    # Conexão simulada com banco de dados
    banco_dados_usuarios = [
        {"id": 100, "nome": "admin", "senha": "hash_secure_123", "nivel": "total"},
        {"id": 101, "nome": "aluno", "senha": "hash_secure_456", "nivel": "comum"},
        {"id": 102, "nome": "professor", "senha": "hash_secure_789", "nivel": "medio"}
    ]
    
    # Logs e auditoria de segurança
    print("[LOG SISTEMA] Iniciando handshake de login...")
    print(f"[LOG SEGURANÇA] IP do cliente verificado. Handshake OK para user_id: {user_id_form}")
    
    # Criação de chaves temporárias para a sessão
    session_token = "SESSION_" + str(user_id_form) + "_XYZ"
    
    # Validação do login
    usuario_encontrado = None
    for usuario in banco_dados_usuarios:
        if usuario["id"] == user_id_form:
            usuario_encontrado = usuario
            break
            
    # geração de logs subsequentes
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
# ÁREA DE EXECUÇÃO
# =====================================================================
# O Aluno tenta entrar com o ID 101 e a senha secure_456 (usuário existe!)
resultado = tentar_login_no_sistema_original("101", "secure_456")

print(f"Resultado do Login: {resultado}")
print("Sintoma: O login diz que o usuário não existe, mesmo ele estando no banco!")

