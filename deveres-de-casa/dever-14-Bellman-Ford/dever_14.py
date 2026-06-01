# Implementação do Algoritmo de Bellman-Ford
# Grafo utilizado conforme especificação:
# A→B(1), A→C(4), B→C(2), B→D(5)
# C→D(1), C→E(3), D→C(-3), D→E(2)
# E→D(1)
# Vértice de origem: A

import math

def bellman_ford(grafo, num_vertices, origem):
    """
    Executa o algoritmo de Bellman-Ford.

    :param grafo: lista de arestas (u, v, peso)
    :param num_vertices: número de vértices
    :param origem: vértice de origem
    :return: (distâncias, predecessores) ou detecta ciclo negativo
    """
    # Inicialização
    dist = {v: math.inf for v in range(num_vertices)}
    pred = {v: None    for v in range(num_vertices)}
    dist[origem] = 0

    iteracoes = []

    print("=" * 60)
    print("   ALGORITMO DE BELLMAN-FORD")
    print("=" * 60)
    print(f"\nVértice de origem: {indice_para_letra(origem)}")
    print(f"Número de vértices: {num_vertices}")
    print(f"Número de arestas: {len(grafo)}\n")

    # Exibe arestas do grafo
    print("Arestas do grafo:")
    for (u, v, w) in grafo:
        print(f"  {indice_para_letra(u)} → {indice_para_letra(v)}  (peso: {w})")

    print()

    # Cabeçalho da tabela de relaxamento
    vertices = list(range(num_vertices))
    letras   = [indice_para_letra(v) for v in vertices]
    col_w    = 8

    linha_sep = "-" * (10 + col_w * num_vertices)
    header    = f"{'Iteração':<10}" + "".join(f"{l:^{col_w}}" for l in letras)

    print("TABELA DE RELAXAMENTO:")
    print(linha_sep)
    print(header)
    print(linha_sep)

    # Estado inicial (iteração 0)
    def formata_dist(d):
        return "∞" if d == math.inf else str(d)

    linha_0 = f"{'0 (início)':<10}" + "".join(
        f"{formata_dist(dist[v]):^{col_w}}" for v in vertices
    )
    print(linha_0)
    iteracoes.append(dict(dist))

    # |V| - 1 iterações de relaxamento
    for i in range(1, num_vertices):
        houve_mudanca = False
        relaxamentos  = []

        for (u, v, w) in grafo:
            if dist[u] != math.inf and dist[u] + w < dist[v]:
                dist_antiga = dist[v]
                dist[v]     = dist[u] + w
                pred[v]     = u
                houve_mudanca = True
                relaxamentos.append(
                    f"  Relaxando {indice_para_letra(u)}→{indice_para_letra(v)}: "
                    f"{formata_dist(dist_antiga)} + {w} = {dist[v]}  →  "
                    f"Atualizar {indice_para_letra(v)} = {dist[v]}"
                )

        linha = f"{i:<10}" + "".join(f"{formata_dist(dist[v]):^{col_w}}" for v in vertices)
        print(linha)

        if relaxamentos:
            for r in relaxamentos:
                print(r)

        iteracoes.append(dict(dist))

        if not houve_mudanca:
            print(f"\n  [Convergiu na iteração {i} — iterações restantes ignoradas]\n")
            break

    print(linha_sep)

    # Detecção de ciclo negativo (|V|-ésima iteração)
    print("\nDETECÇÃO DE CICLO NEGATIVO:")
    print(f"  Executando a {num_vertices}ª iteração (extra)...\n")

    ciclo_negativo = False
    for (u, v, w) in grafo:
        if dist[u] != math.inf and dist[u] + w < dist[v]:
            ciclo_negativo = True
            print(f"  ⚠  Aresta {indice_para_letra(u)}→{indice_para_letra(v)} "
                  f"ainda pode ser relaxada!")

    if ciclo_negativo:
        print("\n  *** CICLO NEGATIVO DETECTADO! ***")
        print("  O grafo contém um ciclo de peso negativo acessível a partir da origem.\n")
    else:
        print("  Nenhum ciclo negativo detectado. Solução ótima encontrada.\n")

    # Resultado final
    print("DISTÂNCIAS MÍNIMAS (origem → destino):")
    print("-" * 40)
    for v in vertices:
        caminho = reconstruir_caminho(pred, origem, v)
        print(f"  {indice_para_letra(origem)} → {indice_para_letra(v)}: "
              f"{formata_dist(dist[v]):<6}  caminho: {caminho}")
    print()

    return dist, pred, ciclo_negativo


def reconstruir_caminho(pred, origem, destino):
    """Reconstrói o caminho mínimo de origem até destino."""
    caminho = []
    atual   = destino
    visitados = set()

    while atual is not None:
        if atual in visitados:
            return "[ciclo detectado]"
        visitados.add(atual)
        caminho.append(indice_para_letra(atual))
        atual = pred[atual]

    caminho.reverse()

    if not caminho or caminho[0] != indice_para_letra(origem):
        return "inalcançável"

    return " → ".join(caminho)


def indice_para_letra(i):
    """Converte índice numérico para letra (0→A, 1→B, ...)."""
    return chr(ord('A') + i)


# ── Grafo da especificação ────────────────────────────────────────────────────
# Vértices: A=0, B=1, C=2, D=3, E=4
# Arestas (u, v, peso)
arestas = [
    (0, 1, 1),   # A→B (1)
    (0, 2, 4),   # A→C (4)
    (1, 2, 2),   # B→C (2)
    (1, 3, 5),   # B→D (5)
    (2, 3, 1),   # C→D (1)
    (2, 4, 3),   # C→E (3)
    (3, 2, -3),  # D→C (-3)
    (3, 4, 2),   # D→E (2)
    (4, 3, 1),   # E→D (1)
]

NUM_VERTICES = 5
ORIGEM       = 0   # A

dist, pred, tem_ciclo = bellman_ford(arestas, NUM_VERTICES, ORIGEM)