altPulo, qntdCano = map(int, input().split())
canos = list(map(int, input().split()))
atual = canos.pop(0)
for cano in canos:
    if max([cano, atual]) - min([cano, atual]) > altPulo:
        print('GAME OVER')
        quit()
    atual = cano
print('YOU WIN')

