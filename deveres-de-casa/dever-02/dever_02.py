import time
import sys

# aumenta o limite de recursão
sys.setrecursionlimit(2000)

# Constantes para teste
TEST_VALUES = [10, 100, 500, 1000]


def factorial(n):
    """
    Calcula o fatorial de um número inteiro utilizando recursão.

    Args:
        n (int): número inteiro não negativo.

    Returns:
        int: valor do fatorial de n.
    """

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


def measure_execution_time():
    """
    Mede o tempo de execução do cálculo de fatorial
    para diferentes valores de n.
    """

    print("\nTempo de execução:")

    for value in TEST_VALUES:
        start_time = time.time()

        factorial(value)

        end_time = time.time()
        execution_time = end_time - start_time

        print(f"n = {value} -> tempo = {execution_time:.6f} segundos")


def main():
    """
    Função principal do programa.
    """

    number = int(input("Digite um número inteiro: "))

    result = factorial(number)

    print(f"Fatorial de {number} é {result}")

    measure_execution_time()


if __name__ == "__main__":
    main()