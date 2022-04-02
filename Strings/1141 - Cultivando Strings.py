from os import system
n = 1
r = []
while n != 0:
    n = int(input())
    a = sorted([input() for x in range(n)], key=len)
    b = a.copy()
    c = 0
    for x in range(0, len(a)):
        if len(b) != 1:
            b.pop(0)
        if f'{a[x]}' in b[0]:
            c += 1
            break
    for x in range(len(a)):
        if len(b) != 1:
            b.pop(0)
        if f'{a[x]}' in b[0]:
            c += 1
            break
    if n != 0:
        r.append(c)
system('cls')
[print(x) for x in r]
