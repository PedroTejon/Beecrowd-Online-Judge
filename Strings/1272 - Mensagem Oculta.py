n = int(input())

for x in range(n):
    frase = input().split()
    letras = [palavra[0] for palavra in frase]
    print(''.join(letras))