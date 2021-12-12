def dijkstra(graph, src):
    distance = {node: (10001, None) for node in graph.keys()}
    distance[src] = (0, src)

    queue = [node for node in graph.keys()]
    while queue:
        upper_bounds = {node: distance[node] for node in queue}
        atual = min(upper_bounds, key=lambda x: upper_bounds[x])
        queue.remove(atual)
        nodosOpcoes = []
        for nodo, distancia in graph[atual]:
            if distance[nodo][0] > distance[atual][0] + distancia:
                nodosOpcoes.append((nodo, distance[atual][0] + distancia, atual))
        if nodosOpcoes:
            nodoDecidido = min(nodosOpcoes, key=lambda x: x[1])
            distance[nodoDecidido[0]] = (nodoDecidido[1], nodoDecidido[2])


    return distance


def main():
    qntdRoteadores, qntdCabos = map(int, input().split())
    graph = {roteador: [] for roteador in range(1, qntdRoteadores + 1)}
    
    for _ in range(qntdCabos):
        roteador1, roteador2, distancia = map(int, input().split())
        graph[roteador1].append((roteador2, distancia))
        graph[roteador2].append((roteador1, distancia))

    distancia = dijkstra(graph, 1)
    print(distancia)
    distance = sorted(distancia.values(), key=lambda x: x[1])
    custo = 0
    for x, nodo in enumerate(distance):
        distance[x] = (nodo[0] - distance[nodo[1] - 1][0], nodo[1])
    print(distance)

if __name__ == "__main__":
    main()