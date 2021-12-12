operador = input()
numeros = [[float(input()) for _ in range(12)] for _ in range(12)]

if operador == 'S':
    print(f'{sum([sum(linha[:x]) for x, linha in enumerate(numeros[:6])]) + sum([sum(linha[:6 - (x + 1)]) for x, linha in enumerate(numeros[6:])]):.1f}')
else:
    print(f'{(sum([sum(linha[:x]) for x, linha in enumerate(numeros[:6])]) + sum([sum(linha[:6 - (x + 1)]) for x, linha in enumerate(numeros[6:])])) / 30:.1f}')