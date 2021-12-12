pares = []
impares = []
for x in range(15):
    i = int(input())
    if i % 2 == 0:
        if len(pares) == 5:
            [print(f'par[{x}] = {pares[x]}') for x in range(5)]
            pares.clear()
        pares.append(i)
    else:
        if len(impares) == 5:
            [print(f'impar[{x}] = {impares[x]}') for x in range(5)]
            impares.clear()
        impares.append(i)
[print(f'impar[{x}] = {impares[x]}') for x in range(len(impares))]
[print(f'par[{x}] = {pares[x]}') for x in range(len(pares))]