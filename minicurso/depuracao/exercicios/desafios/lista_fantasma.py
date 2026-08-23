# =====================================================================
# MINICURSO DE DEPURACAO - DESAFIOS PRATICOS
# Minicurso de Informática para Internet - IFC Concórdia
# Semana de Ensino Pesquisa e Extensão (SEPE)
# =====================================================================

# ---------------------------------------------------------------------
# DESAFIO 2: "A Lista Fantasma"
# Sintoma: O sistema de carrinho de compras acumula produtos de outros
# clientes de forma misteriosa! Cada vez que chamamos a funcao sem passar
# um carrinho, ela traz itens de chamadas anteriores.
# ---------------------------------------------------------------------

def adicionar_ao_carrinho(nome_produto, carrinho=[]):
    """
    Adiciona um novo produto ao carrinho de compras do usuario.
    Se nenhum carrinho for informado, cria um carrinho vazio.
    """
    carrinho.append(nome_produto)
    return carrinho

# Codigo de teste:
print("Cliente 1 adiciona: Celular")
carrinho_c1 = adicionar_ao_carrinho("Celular")
print("Carrinho Cliente 1:", carrinho_c1)  # ['Celular']

print("Cliente 2 adiciona: Notebook")
carrinho_c2 = adicionar_ao_carrinho("Notebook")
print("Carrinho Cliente 2:", carrinho_c2)  # Deveria ser ['Notebook'], mas veio ['Celular', 'Notebook']!
