operador = input()
numeros = [[float(input()) for _ in range(12)] for _ in range(12)]

if operador == 'S':
    print(f'{sum([sum(linha[12 - (x):]) for x, linha in enumerate(numeros)]):.1f}')
else:
    print(f'{sum([sum(linha[12 - (x):]) for x, linha in enumerate(numeros)]) / 66:.1f}')