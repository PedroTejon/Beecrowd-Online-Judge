n = int(input())

for _ in range(n):
    prim, seg = input().split()
    print('encaixa' if prim[-len(seg):] == seg else 'nao encaixa')