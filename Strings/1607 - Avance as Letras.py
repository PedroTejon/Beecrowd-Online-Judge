for _ in range(int(input())):
    print([ord(y) - ord(x) if ord(y) >= ord(x) else (ord(y) - 97) + (26 - (ord(x) - 97)) for x, y in zip(*input().split())])
