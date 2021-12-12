n = int(input())

for x in range(n):
    l = int(input())
    valor = 0
    for elemento in range(l):
        linha = list(map(lambda x: ord(x) % 65, input()))
        for posicao, val in enumerate(linha):
            valor += posicao + val + elemento

    print(valor)