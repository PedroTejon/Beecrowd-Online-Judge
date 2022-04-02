a2 = float(input())
while True:
    a1 = float(input())
    if 0 <= a1 <= 10 and not(0 <= a2 <= 10):
        a2 = a1
        print(f'nota invalida')
    elif 0 <= a1 <= 10 and 0 <= a2 <= 10:
        print(f'media = {(a1 + a2) / 2:.2f}')
        break
    else:
        print(f'nota invalida')
