while True:
    a = int(input())
    if a == 0:
        break
    print(' '.join(map(str, range(1, a + 1))))