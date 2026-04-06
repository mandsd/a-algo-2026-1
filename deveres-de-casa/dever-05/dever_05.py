import math

class ComplexityCalculator:
    """
    Classe para calcular e exibir complexidades de algoritmos e recorrências.
    
    Esta classe utiliza as regras do Teorema Mestre e definições clássicas
    de análise de algoritmos para determinar a notação Big-O.
    """

    def __init__(self):
        """Inicializa a classe de cálculo."""
        self.MARKER = "---"  # Exemplo de constante (SCREAMING_SNAKE_CASE)

    def calculate_merge_sort_complexity(self):
        """
        Retorna a complexidade do algoritmo Merge Sort.
        
        O Merge Sort divide o array em 2 metades e realiza o merge linear.
        Recorrência: T(n) = 2T(n/2) + O(n).
        """
        return "O(n log n)"

    def calculate_matrix_multiplication(self, method="standard"):
        """
        Calcula a complexidade da multiplicação de matrizes.
        
        :param method: Tipo de algoritmo ('standard' ou 'strassen').
        :return: String com a complexidade Big-O.
        """
        if method == "standard":
            return "O(n^3)"
        elif method == "strassen":
            return "O(n^2.81)"
        return "Método desconhecido"

    def master_theorem_solver(self, a, b, fn_degree):
        """
        Resolve recorrências do tipo T(n) = aT(n/b) + n^fn_degree.
        
        Aplica os casos clássicos do Teorema Mestre.
        """
        critical_value = math.log(a, b)

        if fn_degree < critical_value:
            return f"O(n^{critical_value:.1f})"
        elif math.isclose(fn_degree, critical_value):
            return f"O(n^{fn_degree} log n)"
        else:
            return f"O(n^{fn_degree})"

def run_analysis():
    """Função principal para executar as análises solicitadas."""
    calculator = ComplexityCalculator()
    
    # 1) Merge Sort
    print(f"{calculator.MARKER} 1) Algoritmo Merge Sort {calculator.MARKER}")
    print(f"Resultado: {calculator.calculate_merge_sort_complexity()}\n")

    # 2) Multiplicação de Matrizes
    print(f"{calculator.MARKER} 2) Multiplicação de Matrizes {calculator.MARKER}")
    print(f"Padrão: {calculator.calculate_matrix_multiplication('standard')}")
    print(f"Strassen: {calculator.calculate_matrix_multiplication('strassen')}\n")

    # 3) Recorrências
    print(f"{calculator.MARKER} 3) Recorrências {calculator.MARKER}")
    
    # a) T(n) = 2T(n/4) + sqrt(n) -> sqrt(n) é n^0.5. log4(2) = 0.5
    res_a = calculator.master_theorem_solver(2, 4, 0.5)
    print(f"a) T(n) = 2T(n/4) + √n  => {res_a}")

    # b) T(n) = 2T(n/4) + n -> n^1. 1 > log4(2)
    res_b = calculator.master_theorem_solver(2, 4, 1.0)
    print(f"b) T(n) = 2T(n/4) + n   => {res_b}")

    # c) T(n) = 16T(n/4) + n^2 -> n^2. log4(16) = 2
    res_c = calculator.master_theorem_solver(16, 4, 2.0)
    print(f"c) T(n) = 16T(n/4) + n² => {res_c}")

if __name__ == "__main__":
    run_analysis()