n = int(input())

for _ in range(n):
    c = 0
    linha = input()
    esquerda = []
    
    for x, n in enumerate(linha):
        if n == '<':
            esquerda.append(n)
        elif n == '>' and esquerda:
            esquerda.pop()
            c += 1
    
    print(c)
