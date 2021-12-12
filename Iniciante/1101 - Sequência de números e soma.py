while True:
    a, b = map(int, input().split())

    if a <= 0 or b <= 0 or (a <= 0 and b <= 0):
        break

    m = a if a < b else b
    n = b if a < b else a

    c = 0
    for x in range(m, n + 1):
        c += x

    print(f'{" ".join(map(str, range(m, n + 1)))} Sum={c}')