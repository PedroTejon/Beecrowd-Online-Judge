while True:
    a, b = map(int, input().split())
    if a == b:
        break
    else:
        print('Crescente' if a < b else 'Decrescente')