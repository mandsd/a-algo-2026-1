import heapq

grafo = {
    'A': [('B', 4), ('C', 4)],
    'B': [('A', 4), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('E', 6)],
    'D': [('B', 5), ('E', 3), ('F', 4)],
    'E': [('C', 6), ('D', 3), ('F', 2)],
    'F': [('D', 4), ('E', 2)],
}

def prim(grafo, inicio):
    visitados = set()
    arestas_mst = []
    custo_total = 0

    # (custo, origem, destino)
    fila = [(0, inicio, inicio)]

    while fila:
        custo, origem, destino = heapq.heappop(fila)

        if destino in visitados:
            continue

        visitados.add(destino)

        if origem != destino:
            arestas_mst.append((origem, destino, custo))
            custo_total += custo

        for vizinho, peso in grafo[destino]:
            if vizinho not in visitados:
                heapq.heappush(fila, (peso, destino, vizinho))

    return arestas_mst, custo_total

arestas, total = prim(grafo, 'A')

print("Rota dos cabos a serem instalados:")
for origem, destino, custo in arestas:
    print(f"  {origem} --> {destino}: {custo} km")

print(f"\nTotal minimo de cabos: {total} km")
