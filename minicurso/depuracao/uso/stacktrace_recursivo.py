def calcular_fatorial(n):
    breakpoint()
    if n <= 1:
        return 1
    return n * calcular_fatorial(n - 1)

if __name__ == "__main__":
    resultado = calcular_fatorial(5)
    print(resultado)
