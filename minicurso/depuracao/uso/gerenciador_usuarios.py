# =====================================================================
# Minicurso de Informática para Internet - IFC Concórdia
# Semana de Ensino Pesquisa e Extensão (SEPE)
# Arquivo para "brincar" com o painel de depuração.
# =====================================================================

import random

# --- ESTADO GLOBAL DO SISTEMA ---
CONFIG_PERMITIR_CADASTROS = True
MAX_SESSÕES_ATIVAS = 3
SESSÕES_CONECTADAS = []  # Lista global de tokens de usuários conectados

# Banco de dados fictício de usuários (Lista de dicionários)
BANCO_USUARIOS = [
    {"username": "admin", "email": "admin@sistema.org", "perfil": "ADMINISTRADOR", "ativo": True},
    {"username": "mariasilva", "email": "maria@provedor.com", "perfil": "CLIENTE", "ativo": True},
    {"username": "pedro_dev", "email": "pedro@empresa.com", "perfil": "DESENVOLVEDOR", "ativo": False}, # Bloqueado
    {"username": "ana_internet", "email": "ana@escola.edu.br", "perfil": "CLIENTE", "ativo": True}
]

def gerar_token_sessao(usuario):
    """Gera um identificador de sessão aleatório baseado no username."""
    # Reatribuição de string e contas matemáticas básicas
    sufixo_aleatorio = str(random.randint(1000, 9999))
    token = f"SESSION_{usuario.upper()}_{sufixo_aleatorio}"
    return token


def alternar_status_usuario(username):
    """
    Alterna o status do usuário entre ativo/inativo.
    Demonstra troca de valores booleanos e lógica condicional.
    """
    for usuario in BANCO_USUARIOS:
        if usuario["username"] == username:
            # Troca simples de valor lógico
            status_anterior = usuario["ativo"]
            status_novo = not status_anterior
            usuario["ativo"] = status_novo
            print(f"[BD] Status de '{username}' alterado de {status_anterior} para {status_novo}.")
            return True
    return False


def gerenciar_limite_sessoes(novo_token):
    """
    Garante que a lista de sessões ativas não ultrapasse o limite global.
    Demonstra adição e remoção de dados em uma lista global.
    """
    global SESSÕES_CONECTADAS
    
    # Adicionando um item ao final da lista
    SESSÕES_CONECTADAS.append(novo_token)
    print(f"[SESSÃO] Nova sessão registrada: {novo_token}")
    
    # Se estourar o limite, removemos a sessão mais antiga (primeiro da lista)
    while len(SESSÕES_CONECTADAS) > MAX_SESSÕES_ATIVAS:
        # Remoção de dados de uma lista
        sessao_removida = SESSÕES_CONECTADAS.pop(0)
        print(f"[AVISO] Limite de {MAX_SESSÕES_ATIVAS} excedido. Removida sessão antiga: {sessao_removida}")


def realizar_login(username, email_fornecido):
    """
    Valida as credenciais e gera uma sessão ativa.
    Ótimo fluxo para os alunos utilizarem a barra de controle (Step Into / Step Over).
    """
    usuario_encontrado = None
    
    # Normalização de string
    email_limpo = email_fornecido.strip().lower()
    
    # Procura o usuário correspondente
    for usuario in BANCO_USUARIOS:
        if usuario["username"] == username:
            usuario_encontrado = usuario
            break
            
    if not usuario_encontrado:
        print(f"[LOGIN FALHOU] Usuário '{username}' não encontrado no banco de dados.")
        return False, "USUÁRIO_INEXISTENTE"
        
    # Verificação de status lógico
    if not usuario_encontrado["ativo"]:
        print(f"[LOGIN FALHOU] O usuário '{username}' está inativo no momento.")
        return False, "CONTA_BLOQUEADA"
        
    # Verificação simples de email
    if usuario_encontrado["email"].lower() != email_limpo:
        print(f"[LOGIN FALHOU] Email '{email_limpo}' não corresponde ao cadastrado.")
        return False, "EMAIL_INCORRETO"
        
    # Sucesso: Inicialização de sessão
    novo_token = gerar_token_sessao(username)
    gerenciar_limite_sessoes(novo_token)
    
    return True, novo_token


def cadastrar_novo_usuario(username, email, perfil="CLIENTE"):
    """
    Adiciona um novo usuário ao banco em memória caso seja permitido.
    Inspecione a lista BANCO_USUARIOS antes e depois deste fluxo!
    """
    # Reatribuição de string para higienizar dados
    username_limpo = username.strip().replace(" ", "_").lower()
    
    if not CONFIG_PERMITIR_CADASTROS:
        print("[CADASTRO FALHOU] Cadastros globais desabilitados no momento.")
        return False
        
    # Valida se username já existe
    for usuario in BANCO_USUARIOS:
        if usuario["username"] == username_limpo:
            print(f"[CADASTRO FALHOU] Username '{username_limpo}' já está em uso.")
            return False
            
    # Criação de novo dicionário e inserção na lista
    novo_cadastro = {
        "username": username_limpo,
        "email": email.strip().lower(),
        "perfil": perfil.upper(),
        "ativo": True
    }
    
    # Adicionando à lista
    BANCO_USUARIOS.append(novo_cadastro)
    print(f"[BD] Usuário '{username_limpo}' cadastrado com sucesso.")
    return True


if __name__ == "__main__":
    # Inicie a depuração no VS Code para assistir às variáveis mudando em tempo real!
    
    # Passo 1: Tentar efetuar logins diversos (Gerará adição e remoção na lista de sessões globais)
    print("=== TESTANDO FLUXOS DE LOGIN ===")
    sucesso_1, token_1 = realizar_login("mariasilva", "maria@provedor.com")
    sucesso_2, token_2 = realizar_login("ana_internet", "ana@escola.edu.br")
    sucesso_3, token_3 = realizar_login("pedro_dev", "pedro@empresa.com")      # Deve falhar (Inativo)
    sucesso_4, token_4 = realizar_login("admin", "admin@sistema.org")
    
    # Este login estourará o limite e removerá a sessão mais antiga (mariasilva) da lista global
    sucesso_5, token_5 = cadastrar_novo_usuario("carlos souza", "carlos@portal.com")
    if sucesso_5:
        realizar_login("carlos_souza", "carlos@portal.com")
        
    # Passo 2: Reativar o usuário pedro_dev usando a alternação de status (Troca de valores)
    print("\n=== ALTERNANDO STATUS DE CONTAS ===")
    alternar_status_usuario("pedro_dev")
    
    # Tenta logar o Pedro novamente após a ativação (Agora deve funcionar!)
    realizar_login("pedro_dev", "pedro@empresa.com")
    
    print("\n=== LISTA DE SESSÕES ATIVAS FINAL ===")
    print(SESSÕES_CONECTADAS)
