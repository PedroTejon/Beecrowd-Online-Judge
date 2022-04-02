a = int(input())
b = [input() for x in range(a)]

for x in b:
    v = list(map(float, x.split()))
    print(f'{((v[0] * 2) + (v[1] * 3) + (v[2] * 5)) / 10:.1f}')
