n = int(input())
casos = [list(map(int, input().split())) for x in range(n)]
r = 0
for x in casos:
    if x[0] % 2 != 0:
        r += x[0]
        for y in range(1, x[1]):
            r += x[0] + (2 * y)
    else:
        for y in range(x[1]):
            r += (x[0] + 1) + (2 * y)
    print(r)
    r = 0
