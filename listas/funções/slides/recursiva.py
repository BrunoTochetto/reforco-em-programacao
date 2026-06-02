def fatorial(valorAtual):
    # Final recursividade
    if valorAtual == 0:
        return 1
    
    # 5 * 4 * 3 * 2 * 1
    conta = valorAtual * fatorial(valorAtual-1)
    # Final função
    return conta

fatorial(3)

