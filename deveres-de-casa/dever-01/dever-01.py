import random
import time


TAMANHO_LISTA = [1000, 5000, 10000, 20000, 50000]
RANDOM_MIN = 0
RANDOM_MAX = 100000


def insertion_sort(array):
    """
    Ordena uma lista utilizando o algoritmo Insertion Sort.

    Args:
        array (list): Lista de números a ser ordenada.

    Returns:
        list: Lista ordenada.
    """
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

    return array


def generate_random_list(size):
    """
    Gera uma lista de números inteiros aleatórios.

    Args:
        size (int): Tamanho da lista.

    Returns:
        list: Lista com números aleatórios.
    """
    return [
        random.randint(RANDOM_MIN, RANDOM_MAX)
        for _ in range(size)
    ]


def main():
    """
    Executa os testes de desempenho entre
    Insertion Sort e sorted().
    """
    print("Comparação: Insertion Sort vs sorted() (Timsort)")
    print("-" * 60)

    for size in TAMANHO_LISTA:
        original_list = generate_random_list(size)

        list_for_insertion = original_list.copy()
        list_for_sorted = original_list.copy()

        # Mede tempo do Insertion Sort
        start_time = time.time()
        insertion_sort(list_for_insertion)
        end_time = time.time()
        insertion_time = end_time - start_time

        # Mede tempo do sorted()
        start_time = time.time()
        sorted(list_for_sorted)
        end_time = time.time()
        sorted_time = end_time - start_time

        print(f"Tamanho n = {size}")
        print(f"Insertion Sort: {insertion_time:.6f} segundos")
        print(f"sorted():       {sorted_time:.6f} segundos")
        print("-" * 60)


if __name__ == "__main__":
    main()