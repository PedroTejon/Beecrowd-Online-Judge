i = int(input())
r = range(i)
c = 0
for x in range(1000):
    c = 0 if c == i else c
    print(f'N[{x}] = {r[c]}')
    c += 1
