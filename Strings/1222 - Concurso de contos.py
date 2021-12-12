from math import ceil
while True:
    try:
        a, b, c = map(int, input().split())
        texto = input().split()
        char, lin = 0, 1
        for x in texto:
            if len(x) + char <= c:
                char += len(x) + 1
            else:
                char = 0
                char += len(x) + 1
                lin += 1
        print(ceil(lin / b))
    except EOFError:
        break