f = int(input())
n = [100, 50, 20, 10, 5, 2, 1]
print(f)
for x in n:
    print(f'{int(round(f, 2) / x)} nota(s) de R$ {x:.0f},00')
    f -= int(round(f, 2) / x) * x
