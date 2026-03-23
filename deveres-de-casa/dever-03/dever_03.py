"""Módulo para verificação de palíndromos de forma recursiva."""

def verificar_se_palindromo(elementos):
    """
    Verifica se uma lista ou array é um palíndromo usando recursão.

    Args:
        elementos (list): O array de elementos a ser verificado.

    Returns:
        bool: True se for palíndromo, False caso contrário.
    """
    # Caso base: se a lista tem 0 ou 1 elemento, ela é um palíndromo
    if len(elementos) <= 1:
        return True

    # Verifica se os extremos são iguais
    if elementos[0] == elementos[-1]:
        # Chamada recursiva removendo o primeiro e o último elemento
        return verificar_se_palindromo(elementos[1:-1])

    return False


if __name__ == "__main__":
    ARRAY_1 = [0, 1, 2, 3, 2, 1, 0]
    ARRAY_2 = ["a", "b", "b", "a"]
    ARRAY_3 = ["a", "b", "c", "b", "a"]
    ARRAY_4 = ["a", "b", "c", "f", "b", "a"]

    LISTA_TESTES = [ARRAY_1, ARRAY_2, ARRAY_3, ARRAY_4]

    for i, array_atual in enumerate(LISTA_TESTES, 1):
        resultado = "É palíndromo" if verificar_se_palindromo(array_atual) else "Não é palíndromo"
        print(f"array{i} = {array_atual} -> {resultado}")