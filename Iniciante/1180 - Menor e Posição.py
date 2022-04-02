tamanho = int(input())
valores = list(map(int, input().split()))

print(f'Menor valor: {min(valores)}\n'
      f'Posição: {valores.index(min(valores))}')
