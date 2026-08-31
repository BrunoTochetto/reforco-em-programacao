# =====================================================================
# MINICURSO DE DEPURACAO - DESAFIOS PRATICOS
# Minicurso de Informática para Internet - IFC Concórdia
# Semana de Ensino Pesquisa e Extensão (SEPE)
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
        total = preco_unitario - 5 * quantidade
    else:
        total = preco_unitario * quantidade
        
    return total


# Codigo de teste:
preco_item = 50.0
qtd_itens = 12
total = calcular_total_compra(preco_item, qtd_itens)
print(f"Total calculado: R$ {total:.2f} (Esperado: R$ 540.00)")