from string import ascii_uppercase

n = int(input())

for _ in range(n):
    frase = input() 
    posi = int(input())
    valores = list(map(lambda x: ord(x), frase))

    frasenova = ''
    for valor in valores:
        frasenova += ascii_uppercase[valor % 65 - posi]

    print(frasenova)