for x in range(int(input())):
    a, b = input().split()
    maior = a if len(a) >= len(b) else b
    menor = b if len(a) >= len(b) else a
    string = ''
    for y in range(len(maior)):
        try:
            string += a[y] + b[y]
        except IndexError:
            string += maior[y]
    print(string)