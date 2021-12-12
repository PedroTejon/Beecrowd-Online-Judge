def traverse(grid, src, dst):
    queue = [(src, 0)]
    visitados = []

    while len(queue):
        atual = queue.pop(0)
        visitados.append(atual[0])
        ping = atual[1]

        if atual[0] == dst:
            break

        for x in grid[atual[0]]:
            if x[0] not in visitados and x[0] not in queue:
                queue.append((x[0], ping + x[1]))

    return ping

numeroIlhas, quantidadeConexões = map(int, input().split())
grid = {}
for x in range(1, numeroIlhas + 1):
    grid[x] = []

for x in range(quantidadeConexões):
    primeiraIlha, segundaIlha, Ping = map(int, input().split())
    grid[primeiraIlha].append((segundaIlha, Ping))

ilhaInicial = int(input())

pings = []
ilhasTarget = list(grid.keys())
ilhasTarget.remove(ilhaInicial)

for x in ilhasTarget:
    pings.append(traverse(grid, ilhaInicial, x))

print(max(pings) - min(pings))
