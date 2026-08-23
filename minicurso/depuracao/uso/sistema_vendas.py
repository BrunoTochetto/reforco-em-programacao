# =====================================================================
# Minicurso de Informática para Internet - IFC Concórdia
# Semana de Ensino Pesquisa e Extensão (SEPE)
# Arquivo para "brincar" com o painel de depuração.
# =====================================================================

import time

# --- VARIÁVEIS GLOBAIS ---
SISTEMA_ATIVO = True
TAXA_IMPOSTO_PADRAO = 0.08  # 8%
CUPOM_DESCONTO_GLOBAL = "FESTA15"
LOGS_PROCESSAMENTO = []

# Banco de dados simulado em memória
ESTOQUE_PRODUTOS = [
    {"id": 1, "nome": "Teclado Mecânico", "preco": 250.00, "qtd": 15},
    {"id": 2, "nome": "Mouse Gamer", "preco": 180.00, "qtd": 3},
    {"id": 3, "nome": "Monitor UltraWide", "preco": 1200.00, "qtd": 5},
    {"id": 4, "nome": "Headset USB", "preco": 320.00, "qtd": 0},  # Sem estoque
    {"id": 5, "nome": "Mousepad Speed", "preco": 80.00, "qtd": 25}
]

def registrar_log(mensagem):
    """Adiciona uma mensagem formatada à lista global de logs."""
    timestamp = time.strftime("%H:%M:%S")
    # Reatribuição de string para formatação
    log_formatado = f"[{timestamp}] {mensagem.upper()}"
    LOGS_PROCESSAMENTO.append(log_formatado)


def verificar_e_atualizar_estoque(produto_id, quantidade_desejada):
    """
    Verifica se há estoque suficiente e subtrai a quantidade desejada.
    Demonstra modificação de listas e dicionários.
    """
    registrar_log(f"Verificando estoque do produto ID {produto_id}")
    
    for produto in ESTOQUE_PRODUTOS:
        if produto["id"] == produto_id:
            estoque_atual = produto["qtd"]
            
            if estoque_atual >= quantidade_desejada:
                # Contas com números
                novo_estoque = estoque_atual - quantidade_desejada
                produto["qtd"] = novo_estoque
                registrar_log(f"Estoque atualizado para '{produto['nome']}': {novo_estoque} restantes")
                return True, produto["nome"], produto["preco"]
            else:
                registrar_log(f"Falha de estoque para produto ID {produto_id}. Desejado: {quantidade_desejada}, Em estoque: {estoque_atual}")
                return False, produto["nome"], 0.0
                
    registrar_log(f"Produto ID {produto_id} não encontrado no estoque.")
    return False, "Desconhecido", 0.0


def aplicar_desconto_e_impostos(subtotal, cupom):
    """
    Aplica regras de desconto e imposto.
    Excelente para inspecionar variáveis locais em operações matemáticas.
    """
    breakpoint()
    desconto = 0.0
    
    # Validação e reatribuição de string
    cupom_limpo = cupom.strip().upper()
    
    if cupom_limpo == CUPOM_DESCONTO_GLOBAL:
        desconto = subtotal * 0.15  # 15% de desconto
        registrar_log(f"Cupom de desconto global '{CUPOM_DESCONTO_GLOBAL}' aplicado com sucesso.")
    elif cupom_limpo == "BOASVINDAS":
        desconto = 50.00  # R$ 50 fixo
        registrar_log("Cupom 'BOASVINDAS' aplicado.")
    else:
        registrar_log("Nenhum cupom válido fornecido.")
        
    # Garantir que o desconto não seja maior que o subtotal
    if desconto > subtotal:
        desconto = subtotal
        
    total_com_desconto = subtotal - desconto
    imposto = total_com_desconto * TAXA_IMPOSTO_PADRAO
    total_final = total_com_desconto + imposto
    
    return desconto, imposto, total_final


def ordenar_precos_extremos(preco_a, preco_b):
    """
    Exemplo clássico de troca de valores em variáveis (swap).
    Garante que preco_a seja sempre o menor e preco_b o maior.
    """
    if preco_a > preco_b:
        registrar_log("Invertendo valores para ordenação interna de limites de preço.")
        # Troca de valores em variáveis
        preco_a, preco_b = preco_b, preco_a
    return preco_a, preco_b


def processar_pedido_compra(cliente, itens_carrinho, cupom=""):
    """
    Função principal que coordena o processamento do pedido de compra.
    Incorpore breakpoints aqui para observar o painel de depuração do VS Code se preenchendo.
    """
    registrar_log(f"Iniciando processamento de pedido para o cliente: {cliente}")
    
    itens_processados = []
    subtotal_pedido = 0.0
    
    # Iteração sobre a lista de itens do carrinho
    breakpoint()
    for item in itens_carrinho:
        id_prod = item["produto_id"]
        qtd_solicitada = item["qtd"]
        
        sucesso, nome_prod, preco_unitario = verificar_e_atualizar_estoque(id_prod, qtd_solicitada)
        
        if sucesso:
            # Cálculos aritméticos
            valor_item = preco_unitario * qtd_solicitada
            subtotal_pedido += valor_item
            
            itens_processados.append({
                "produto": nome_prod,
                "qtd": qtd_solicitada,
                "valor_total": valor_item
            })
        else:
            registrar_log(f"Item '{nome_prod}' foi ignorado por falta de estoque.")
            
    if not itens_processados:
        registrar_log("Pedido cancelado: nenhum item aprovado no estoque.")
        return None
        
    # Aplicação financeira
    desconto, imposto, total_final = aplicar_desconto_e_impostos(subtotal_pedido, cupom)
    
    # Simulação de verificação de preços limites
    menor_valor, maior_valor = ordenar_precos_extremos(subtotal_pedido, total_final)
    
    pedido_finalizado = {
        "cliente": cliente.strip(),
        "itens": itens_processados,
        "financeiro": {
            "subtotal": subtotal_pedido,
            "desconto": desconto,
            "imposto": imposto,
            "total_a_pagar": total_final,
            "faixa_precos": (menor_valor, maior_valor)
        },
        "status": "APROVADO_E_FATURADO"
    }
    
    registrar_log(f"Pedido faturado com sucesso para {cliente}. Total a pagar: R$ {total_final:.2f}")
    return pedido_finalizado


if __name__ == "__main__":

    # Insiram um Breakpoint na linha abaixo ('carrinho_exemplo = ...') e apertem F5
    # SELECIONANDO O PYTHON DEBUGGER
    
    # 1. Definindo dados do carrinho
    carrinho_exemplo = [
        {"produto_id": 1, "qtd": 2},  # Teclado Mecânico (R$ 250 cada) -> OK
        {"produto_id": 2, "qtd": 4},  # Mouse Gamer (R$ 180 cada) -> Solicita 4 mas só tem 3! -> FALHA
        {"produto_id": 5, "qtd": 1}   # Mousepad Speed (R$ 80 cada) -> OK
    ]
    
    # 2. Processando o pedido
    pedido_resultado = processar_pedido_compra(
        cliente="  João da Silva de Souza  ", 
        itens_carrinho=carrinho_exemplo, 
        cupom="festa15"
    )
    
    # 3. Exibindo resultados finais
    print("\n--- RESULTADO DO PROCESSAMENTO ---")
    if pedido_resultado:
        print(f"Cliente: {pedido_resultado['cliente']}")
        print(f"Status do Pedido: {pedido_resultado['status']}")
        print(f"Total a Pagar: R$ {pedido_resultado['financeiro']['total_a_pagar']:.2f}")
    else:
        print("Pedido não pôde ser gerado.")
        
    print("\n--- LOGS GERADOS ---")
    for log in LOGS_PROCESSAMENTO:
        print(log)
