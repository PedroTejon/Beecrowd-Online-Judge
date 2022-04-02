coluna = int(input())
operador = input()
numeros = [[float(input()) for _ in range(12)] for _ in range(12)]

if operador == 'S':
    print(f'{sum([linha[coluna] for linha in numeros]):.1f}')
else:
    print(f'{sum([linha[coluna] for linha in numeros]) / 12:.1f}')