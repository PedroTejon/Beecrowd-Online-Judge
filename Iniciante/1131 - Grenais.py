parar = False
c = 0
g, i, e = 0, 0, 0
while parar is not True:
    golInter, golGremio = map(int, input().split())
    c += 1
    g += 1 if golInter < golGremio else 0
    i += 1 if golInter > golGremio else 0
    e += 1 if golInter == golGremio else 0
    while True:
        print('Novo grenal (1-sim 2-nao)')
        continuar = int(input())
        if continuar == 1:
            break
        elif continuar == 2:
            parar = True
            break
if i > g:
    who = 'Inter venceu mais'
elif i < g:
    who = 'Gremio venceu mais'
else:
    who = 'Nao houve vencedor'
print(f'{c} grenais\n'
      f'Inter:{i}\n'
      f'Gremio:{g}\n'
      f'Empates:{e}\n'
      f'{who}')