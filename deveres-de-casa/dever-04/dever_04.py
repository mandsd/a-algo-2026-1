import math

VALOR_LIMITE_AVISO = 25

def calcular_funcao_recursiva(n):
    """
    Calcula o valor da função F(n) = 2*F(n-1) + n^2 de forma recursiva.

    Args:
        n (int): O termo da sequência a ser calculado. Deve ser n >= 1.

    Returns:
        float: O valor resultante da função para o termo n.
    """
    # Caso base: F(1) = 2
    if n == 1:
        return 2.0
    
    # Passo recursivo: F(n) = 2 * F(n-1) + n^2
    resultado_recursivo = calcular_funcao_recursiva(n - 1)
    return 2 * resultado_recursivo + math.pow(n, 2)

def main():
    """
    Ponto de entrada do programa. Solicita entrada do usuário e exibe o resultado.
    """
    try:
        valor_n = int(input("Digite um valor para n: "))
        
        if valor_n < 1:
            print("Erro: O valor de n deve ser pelo menos 1.")
        else:
            if valor_n > VALOR_LIMITE_AVISO:
                print(f"Aviso: n={valor_n} pode demorar devido à complexidade O(2^n).")
            
            resultado = calcular_funcao_recursiva(valor_n)
            print(f"O resultado de F({valor_n}) é: {resultado}")
            
    except ValueError:
        print("Erro: Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    main()