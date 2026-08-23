def fatorial(valorAtual):
    # Final recursividade
    if valorAtual == 0:
        return 1
    
    # 5 * 4 * 3 * 2 * 1
    conta = valorAtual * fatorial(valorAtual-1)
    # Final função
    return conta

fatorial(5)




def somarCoelho(coelhos):
    if coelhos == 0:
        return 0
    
    conta = 2 + somarCoelho(coelhos-1)
    
    return conta



