a, b, c = map(float, input().split())

if a < b + c and b < a + c and c < a + b:
    print(f'Perimetro = {a + b + c:.1f}')
else:
    print(f'Area = {((a + b) * c) / 2:.1f}')


