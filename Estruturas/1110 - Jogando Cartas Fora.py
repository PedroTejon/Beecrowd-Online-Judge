while True:
    n = int(input())

    if n == 0:
        break

    lista = list(range(1, n + 1))
    descartadas = []
    while len(lista) != 1:
        primeira = lista.pop(0)
        descartadas.append(primeira)
        segunda = lista.pop(0)
        lista.append(segunda)
    print(f'Discarded cards: {", ".join(map(str, descartadas))}\nRemaining card: {lista[0]}')
            