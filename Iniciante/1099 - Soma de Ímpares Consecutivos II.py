for x in range(int(input())):
    a, b = map(int, input().split())
    r = 0
    if a < b:
        for x in range(a + 1, b):
            if x % 2 != 0:
                r += x
    elif a >= b:
        for x in range(a - 1, b, -1):
            if x % 2 != 0:
                r += x
    print(r)