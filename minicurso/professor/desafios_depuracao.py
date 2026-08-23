# =====================================================================
# MINICURSO DE DEPURACAO - DESAFIOS PRATICOS
# Minicurso para alunos de informatica para Internet
# =====================================================================

# ---------------------------------------------------------------------
# DESAFIO 1: "O Desconto Misterioso"
# Sintoma: O valor total da compra fica negativo ou absurdo quando
# o cliente compra mais de 10 itens!
# ---------------------------------------------------------------------

def calcular_total_compra(preco_unitario, quantidade):
    """
    Calcula o valor total de uma compra. Se o cliente comprar mais de
    10 itens, ele deveria ganhar um desconto de R$ 5,00 no preco de CADA item.
    """
    if quantidade > 10:
        # BUG DE PRECEDENCIA DE OPERADORES
        # O programador queria fazer: (preco_unitario - 5) * quantidade
        # Mas sem os parenteses, o Python multiplica primeiro!
        total = preco_unitario - 5 * quantidade
    else:
        total = preco_unitario * quantidade
        
    return total

# Instrucoes para o aluno:
# 1. Execute o arquivo e veja o erro acontecer de forma direta (determinista).
# 2. Insira 'breakpoint()' dentro da funcao calcular_total_compra.
# 3. Use o comando 'p' para inspecionar as variaveis e descubra por que o total deu negativo.
# 4. Corrija o bug aplicando a precedencia correta (parenteses).

# Codigo de teste do aluno:
preco_item = 50.0
qtd_itens = 12
total = calcular_total_compra(preco_item, qtd_itens)
print(f"Total calculado: R$ {total:.2f} (Esperado: R$ 540.00)")


# ---------------------------------------------------------------------
# DESAFIO 2: "A Lista Fantasma" (Heisenbug)
# Sintoma: O sistema de carrinho de compras acumula produtos de outros
# clientes de forma misteriosa! Cada vez que chamamos a funcao sem passar
# um carrinho, ela traz itens de chamadas anteriores.
# ---------------------------------------------------------------------

def adicionar_ao_carrinho(nome_produto, carrinho=[]):
    """
    Adiciona um novo produto ao carrinho de compras do usuario.
    Se nenhum carrinho for informado, cria um carrinho vazio.
    """
    # BUG DE ARGUMENTO PADRAO MUTAVEL (Heisenbug)
    # Em Python, argumentos padrao sao avaliados apenas uma vez, na definicao
    # da funcao. Isso faz com que a lista 'carrinho' seja compartilhada por todos!
    carrinho.append(nome_produto)
    return carrinho

# Instrucoes para o aluno:
# 1. Execute as chamadas abaixo e observe como o "carrinho" acumula produtos
#    de clientes diferentes que deveriam ter carrinhos separados e vazios.
# 2. Adicione 'breakpoint()' logo no inicio da funcao adicionar_ao_carrinho.
# 3. No terminal do debugger (Pdb), use 'p id(carrinho)' para ver o endereco de memoria da lista.
# 4. Avance e repita o processo para a proxima chamada. Note que o ID de memoria e o mesmo!
# 5. Corrija o bug usando a boa pratica: 'carrinho=None' e inicializando
#    'if carrinho is None: carrinho = []' dentro da funcao.

# Codigo de teste do aluno:
# print("Cliente 1 adiciona: Celular")
# carrinho_c1 = adicionar_ao_carrinho("Celular")
# print("Carrinho Cliente 1:", carrinho_c1)  # ['Celular']
# 
# print("\nCliente 2 adiciona: Notebook")
# carrinho_c2 = adicionar_ao_carrinho("Notebook")
# print("Carrinho Cliente 2:", carrinho_c2)  # Deveria ser ['Notebook'], mas veio ['Celular', 'Notebook']!


# ---------------------------------------------------------------------
# DESAFIO 3: "O Validador de Usuarios Silencioso" (Schroedinbug)
# Sintoma: Um validador de cadastros para sistemas web que parece funcionar
# perfeitamente, mas se comporta de forma inesperada ou falha silenciosamente
# sob certas combinacoes de strings.
# ---------------------------------------------------------------------

def validar_dados_cadastro(email, senha):
    """
    Valida se o email possui arroba (@) antes do dominio (.com ou .org)
    e se a senha possui o tamanho minimo de 8 caracteres.
    Retorna True se valido, ou False se invalido.
    """
    # BUG SILENCIOSO / ERRO DE DESIGN (Schroedinbug)
    # Se o email contiver '.com' e '@', mas o '.com' vier ANTES do '@'
    # (ex: "meu.com@usuario"), a validacao falha ou passa incorretamente?
    # E se a senha for None ou nao for string? O programa quebra de forma abrupta!
    
    if len(senha) < 8:
        return False
        
    # Bug logico: apenas verifica se as substrings existem, mas nao a ordem!
    # Um email como "contato.com@empresa" passara incorretamente nesta verificacao simples.
    if "@" not in email or (".com" not in email and ".org" not in email):
        return False
        
    # Outro bug potencial: se o email nao for string, 'in' lanca TypeError.
    return True

# Instrucoes para o aluno:
# 1. Teste o validador com entradas incomuns, como "contato.com@empresa" ou "admin@dominio.org.br".
# 2. Use 'breakpoint()' para pausar a execucao e inspecionar a ordem das substrings
#    usando metodos como 'email.index("@")' e 'email.index(".com")'.
# 3. Pense como um desenvolvedor web: como garantir que a estrutura seja email@dominio.extensao?
# 4. Melhore o validador para tratar erros de tipo (ex: senha sendo None) usando try-except.

# Codigo de teste do aluno:
# print("Cadastro 1 (Valido):", validar_dados_cadastro("aluno@escola.com", "senha123"))
# print("Cadastro 2 (Invalido mas passa!):", validar_dados_cadastro("escola.com@aluno", "12345678"))
