a = 0
p = []
d = [float(input()) for x in range(6)]
for x in d:
    a += 1 if x >= 0 else 0
    if x >= 0:
        p.append(x)
print(f'{a} valores positivos')
print(f'{sum(p) / a:.1f}')
