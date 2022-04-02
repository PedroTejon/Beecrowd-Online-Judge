from math import sqrt
a, b, c = map(float, input().split())
try:
    delta = sqrt((b ** 2) - (4 * a * c))
    print(f'R1 = {(- b + delta) / (2 * a):.5f}\n'
          f'R2 = {(- b - delta) / (2 * a):.5f}')
except:
    print('Impossivel calcular')