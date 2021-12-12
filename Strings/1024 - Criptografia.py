for x in range(int(input())):
    a = input()
    b = c = ''
    for y in a:
        b += chr(int(ord(y)) + 3) if y.isalpha() else y
    for y in range(len(b) - 1, -1, -1):
        c += b[y]
    r = c[:int(len(c) / 2)]
    for y in range(int(len(c) / 2), len(c)):
        r += chr(int(ord(c[y])) - 1)
    print(r)
