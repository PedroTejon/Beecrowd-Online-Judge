matriz = []
linha = int(input())
operacao = input()

for y in range(12):
    i = f'{input()} {input()} {input()} {input()} {input()} {input()} {input()} {input()} {input()} {input()} {input()} {input()}'
    matriz.append(list(map(float, i.split())))

print(f'{sum(matriz[linha]):.1f}' if operacao == 'S' else f'{sum(matriz[linha])/12:.1f}')
